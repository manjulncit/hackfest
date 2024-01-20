> Clone this project and navigate to the main directory (hackfest)

    cd hackfest

> Create and activate new virtual environment

	mkvirtualenv hackfestenv
    pip install -r requirements.txt


> Navigate to hackfest inside of the main directory.

	cd hackfest

> Setup initial database and create required tables and data for default applications according to the sequence

	Create a new db name db_hackfest (or your choice)

    Executee 01_db_hackfest.sql in the database using phpmyadmin or any other client.


> Create a file as .env in the root folder for the environment variables based on the env.example

    env.example
    DB_HOST = 'localhost'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_NAME = ''


> Run the application

    cd hackfest/code
    python app.py

    This will run application in 3000 port by default. Open http//:127.0.0.1:8000 in browser
