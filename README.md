# Code-IT Suisse

A Django app, deployed to Heroku.


## Running Locally


```sh
$ git clone git@github.com:krohak/codeIT-Suisse.git
$ cd python-getting-started

$ pipenv install

$ createdb codeIT-Suisse

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

