Quotations
================================

[![Build Status](https://travis-ci.org/jessamynsmith/quotations.svg?branch=master)](https://travis-ci.org/jessamynsmith/quotations)
[![Coverage Status](https://coveralls.io/repos/jessamynsmith/quotations/badge.svg?branch=master)](https://coveralls.io/r/jessamynsmith/quotations?branch=master)

Simple site that serves a page with a random quotation and allows searching of quotations.
Also provides a quotation API. Check out the live app:
https://underquoted.herokuapp.com/
You can inspect the API at:
https://underquoted.herokuapp.com/api/v1/quotations/schema/?format=json

Development
-----------

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/quotations.git

Create a virtualenv and install dependencies:

    mkvirtualenv quotations
    pip install -r requirements/development.txt

Use dev settings:

    export DJANGO_SETTINGS_MODULE=quotations.settings.development

Set up db:

    python manage.py syncdb
    python manage.py migrate

Run tests and view coverage:

     coverage run manage.py test quotations
     coverage report

Check code style:

    flake8

Run server:

    python manage.py runserver
