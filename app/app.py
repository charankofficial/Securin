from flask import Flask, request, jsonify, render_template
import requests
import mysql.connector
from datetime import datetime, timedelta

app = Flask(__name__)

def db_config():
    return {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'cve_db'
    }

def init_db():
    conn = mysql.connector.connect(**db_config())
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cve (
                        id VARCHAR(50) PRIMARY KEY,
                        identifier TEXT,
                        published_date DATETIME,
                        last_modified_date DATETIME,
                        status VARCHAR(50)
                      )''')
    conn.commit()
    conn.close()

init_db()

def fetch_cve_data(offset=0, limit=10):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex={offset}&resultsPerPage={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/sync_cves', methods=['GET'])
def sync_cves():
    offset = 0
    limit = 100
    conn = mysql.connector.connect(**db_config())
    cursor = conn.cursor()

    try:
        while True:
            data = fetch_cve_data(offset, limit)
            if not data or "vulnerabilities" not in data:
                break

            for cve_item in data.get("vulnerabilities", []):
                cve_id = cve_item["cve"]["id"]
                identifier = cve_item["cve"]["sourceIdentifier"]
                published_date = cve_item["cve"]["published"]
                last_modified_date = cve_item["cve"]["lastModified"]
                status = cve_item["cve"]["vulnStatus"]

                cursor.execute('''INSERT INTO cve (id, identifier, published_date, last_modified_date, status)
                                  VALUES (%s, %s, %s, %s, %s)
                                  ON DUPLICATE KEY UPDATE
                                  identifier = VALUES(identifier),
                                  published_date = VALUES(published_date),
                                  last_modified_date = VALUES(last_modified_date),
                                  status = VALUES(status)''',
                               (cve_id, identifier, published_date, last_modified_date, status))
            offset += limit
            if len(data["vulnerabilities"]) < limit:
                break

        conn.commit()
    finally:
        conn.close()

    return jsonify({"message": "CVE data synchronized successfully."})

@app.route('/cves', methods=['GET'])
def get_cves():
    conn = mysql.connector.connect(**db_config())
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM cve WHERE 1=1"
    params = []

    cve_id = request.args.get('cve_id')
    if cve_id:
        query += " AND id = %s"
        params.append(cve_id)

    year = request.args.get('year')
    if year:
        query += " AND YEAR(published_date) = %s"
        params.append(year)

    status = request.args.get('status')
    if status:
        query += " AND status >= %s"
        params.append(status)

    days = request.args.get('days')
    if days:
        cutoff_date = datetime.now() - timedelta(days=int(days))
        query += " AND last_modified_date >= %s"
        params.append(cutoff_date.strftime('%Y-%m-%d'))

    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit
    query += " LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return jsonify(results)

@app.route('/cves/list')
def cve_list():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
