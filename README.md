# Career-Insights
This is the W4111 database course project. We would like to develop a web server for Columbia students to share their internship, interview, full-time working or any career-related experiences. This project forbids the use of ORM, so we are writing raw sql queries.
## Overview
* The sql folder contain the raw sql statements to create, populate, and perform some queries on the tables in the database, which is also part of the project requirement.
* The server folder contains the code for the flask web server.
* Python3.5+ and postgres is required.
## Usage
1. (Optional) Use sql/create.sql and/or sql/insert.sql to populate the postgres database.
2. Create a virtual environment inside server folder and install required packages.
    ```
    $ cd server
    $ python3 -m venv venv
    $ . venv/bin/activate
    (venv)$ pip install flask sqlalchemy psycopg2
    ```
3. Configure server/config.cfg to connect to the postgres database.
4. Run the server locally.
    ```
    $ cd server
    $ . venv/bin/activate
    (venv)$ python app.py
    ```
    or
    ```
    $ cd server
    $ ./run.sh
    ```
## Screenshots
<div float="left">
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot1.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot2.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot3.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot4.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot5.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot6.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot7.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot8.png?raw=true" width="32%"/>
  <img src="https://github.com/Terry1004/Career-Insights/blob/master/screenshots/flask-screenshot9.png?raw=true" width="32%"/>
</div>
