#!/bin/bash

# This script will quit on the first error that is encountered.
set -e

CIRCLE=$1

DEPLOY_DATE=`date "+%FT%T%z"`
SECRET=$(openssl rand -base64 58 | tr '\n' '_')

heroku config:set --app=underquoted \
NEW_RELIC_APP_NAME='underquoted' \
ADMIN_EMAIL="the.underquoted@gmail.com" \
ADMIN_NAME="the.underquoted" \
DJANGO_SECRET_KEY="$SECRET" \
DEPLOY_DATE="$DEPLOY_DATE" \
> /dev/null

if [ $CIRCLE ]
then
    git push https://heroku:$HEROKU_API_KEY@git.heroku.com/underquoted.git master
else
    git push heroku master
fi

heroku run python manage.py migrate --noinput --app=underquoted
