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


In addition the process is as folllows

Process: 
step 1 : I retrieved datas from the API Url provided and set a limit of 10 to retrieve and got a offset data to be retrived 
step 2: once the data is visited or clicked next the api will send a reuest to the api url and store the datas without dupliction 
step 3 : This will enhance the database storage and the database will be stored once the user visited the data and the datas i stored in database will have only the constraints whatever gven in question 
in Addition to step 3: if suppose we need to store the all dtas we have to use nosql like frebase to store that much od datas in order to retrieve it and access in sql we have to use only some local storage since we cant handle that much of attribues in a single table
step 4: in front end used javascript for pagination control and data limit offset 
step 6 : using flask and mysql localhost created a link between them and stoired retirved data and send the data to the frontend 
step 6: called a flask and registerd a blueprint name app and used to return the blueprint as a module 
step 7: using the score of the database we can render the data once the user visited the page 
step 8: interlink the datas and fetch using a dict variable and parse to the dict variable and send the data to the front end 


conclusion:
The Api(Flask) will manage the request and response whatever routed and the user will able to retrieve and see data as per the choice given (eg.10,50,100) and pagination will render the each data once the next is clicked
the datas will be rendered from api if there is no more datas in the database 

note:
since 2 lakshs datas cant be load and stored in a local database we couldnt process the full data retrieval once the data needed the api will send the request to the npm webpage and process the data into the 
database.
Due to some time constraint i cant create a proper blueprint like struct
i added database connectivity inside the app.py and i supposed to do the separate file and call the function inside the app.py will be efficient to use the blueprint for flask .

