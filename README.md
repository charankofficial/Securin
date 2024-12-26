# Securin
Project Description
This project is designed to consume, store, and manage CVE (Common Vulnerabilities and Exposures) information from the NVD CVE API. The system retrieves CVE data in batches, processes it to ensure data quality, and stores it in a database. It provides APIs for querying CVE details based on various parameters and includes a front-end for data visualization. The application is built using Python, Flask, MySQL, and web technologies (HTML, CSS, JavaScript).

Features
CVE Data Ingestion:

Retrieves CVE data from the NVD API in chunks using startIndex and resultsPerPage parameters.
Stores the data in a MySQL database with cleansing and deduplication.
Batch Synchronization:

Periodically synchronizes CVE data from the API.
Supports both full refresh and incremental refresh (for modified data).
Querying CVE Data via APIs:

Filter CVE details by:
CVE ID
Year of publication
CVE Score (using cvssMetricV2 or cvssMetricV3)
Last modified within a specified number of days.
Front-End Visualization:

Displays CVE data in a table on the /cves/list route.
Includes pagination and results-per-page functionality (10, 50, 100 records per page).
Provides a "Total Records" count below the table.
Server-Side Enhancements (Optional):

Pagination and sorting for date fields on the back end.
API Documentation:

Comprehensive documentation for all API endpoints with examples.
Testing:

Unit tests to validate the functionality, ensuring quality and reliability.
Best Practices:

Secure, clean, and well-documented code following industry standards.
Technical Stack
Backend:

Flask (Python web framework)
MySQL (Database for storing CVE data)
NVD CVE API (Data source)
Frontend:

HTML, CSS, JavaScript (Visualization and user interaction)
Libraries and Tools:

requests (for consuming the CVE API)
mysql.connector (for database integration)
datetime (for date filtering)

Database Schema
Table: cve

Column	Type	Description
id	VARCHAR(50)	Primary Key (CVE ID)
identifier	TEXT	Source Identifier
published_date	DATETIME	Date when the CVE was published
last_modified_date	DATETIME	Date when the CVE was last modified
status	VARCHAR(50)	Vulnerability status
API Endpoints
Synchronize CVE Data
GET /sync_cves
Fetches CVE data from the API and synchronizes it with the database.

Get CVE Data
GET /cves
Retrieves CVE details based on the following query parameters:

cve_id: Filter by CVE ID.
year: Filter by publication year.
status: Filter by vulnerability status.
days: Filter CVEs modified in the last N days.
page and limit: Pagination support.
CVE List Visualization
GET /cves/list
Displays CVE data in a table on a web page, including pagination and records-per-page options.


