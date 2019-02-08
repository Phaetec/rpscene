# rpscene

## How to run

This project uses [Pipenv](https://github.com/pypa/pipenv) to provide a virtual environment and dependency management.
Additionally npm is used for CSS and JS frameworks.
To setup the virtual environment and install all required dependencies within this environment, simply run
```
$ pipenv install
$ npm install --prefix static
```

To run the Django server within the virtual environment, run
```
$ pipenv run python manage.py runserver
```

To work in the virtual environment, run
```
$ pipenv shell
```
