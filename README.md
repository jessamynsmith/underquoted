# Underquoted

[![Build Status](https://circleci.com/gh/jessamynsmith/underquoted.svg?style=shield)](https://circleci.com/gh/jessamynsmith/underquoted)
[![Coverage Status](https://coveralls.io/repos/jessamynsmith/underquoted/badge.svg?branch=master)](https://coveralls.io/r/jessamynsmith/underquoted?branch=master)

Simple site that serves a page with a random quotation and allows searching of quotations.
Also provides a quotation API. Check out the live app:
https://underquoted.herokuapp.com/
You can inspect the API at:
https://underquoted.herokuapp.com/api/v1/quotations/schema/?format=json

## Retrieve Quotes

You can use curl to search quotes on the live server:

    curl -vk -X GET -H "Content-Type: application/json" "https://underquoted.herokuapp.com/api/v2/quotations/?search=busy"

## Development

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/underquoted.git

Create a virtualenv using Python 3 and install dependencies. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv underquoted --python=/path/to/python3
    pip install -r requirements.txt
    
If psycopg2 complains about missing SSL on OSX:

    LDFLAGS="-L/usr/local/opt/openssl/lib" pip install -r requirements.txt
    
Create database (you must have PostgreSQL installed):

    createdb underquoted
    psql underquoted
    
In psql:

    CREATE EXTENSION unaccent;
    ALTER FUNCTION unaccent(text) IMMUTABLE;

Set environment variables as desired. DATABASE_URL is required. Recommended dev settings:

    export DATABASE_URL=postgres://<username>@127.0.0.1:5432/underquoted
    export DJANGO_DEBUG=1
    export DJANGO_ENABLE_SSL=0

Set up db:

    python manage.py syncdb
    python manage.py migrate

Run tests and view coverage:

     coverage run manage.py test
     coverage report

Check code style:

    flake8

Run server:

    python manage.py runserver
    
    
## Continuous Integration and Deployment

This project is already set up for continuous integration and deployment using circleci, coveralls,
and Heroku.

Make a new Heroku app, and add the following addons:

    Heroku Postgres
	SendGrid
	New Relic APM
	Papertrail

Enable the project on coveralls.io, and copy the repo token

Enable the project on circleci.io, and under Project Settings -> Environment variables, add:

    COVERALLS_REPO_TOKEN <value_copied_from_coveralls>
    
On circleci.io, under Project Settings -> Heroku Deployment, follow the steps to enable
Heroku builds. At this point, you may need to cancel any currently running builds, then run
a new build.


