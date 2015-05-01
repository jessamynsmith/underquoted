Underquoted
===========

[![Build Status](https://circleci.com/gh/jessamynsmith/underquoted.svg?style=shield)](https://circleci.com/gh/jessamynsmith/underquoted)
[![Coverage Status](https://coveralls.io/repos/jessamynsmith/underquoted/badge.svg?branch=master)](https://coveralls.io/r/jessamynsmith/underquoted?branch=master)

Simple site that serves a page with a random quotation and allows searching of quotations.
Also provides a quotation API. Check out the live app:
https://underquoted.herokuapp.com/
You can inspect the API at:
https://underquoted.herokuapp.com/api/v1/quotations/schema/?format=json

Development
-----------

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/underquoted.git

Create a virtualenv and install dependencies:

    mkvirtualenv underquoted --python=/path/to/python3
    pip install -r requirements/development.txt

Use development settings:

    export DJANGO_SETTINGS_MODULE=underquoted.settings.development

Set up db (you must have PostgreSQL installed):

    python manage.py syncdb
    python manage.py migrate
    
    In psql:
    CREATE EXTENSION unaccent;
    ALTER FUNCTION unaccent(text) IMMUTABLE;

Run tests and view coverage:

     coverage run manage.py test
     coverage report

Check code style:

    flake8

Run server:

    python manage.py runserver
