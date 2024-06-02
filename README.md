# CommunityCare API
Community census API


## Installation
windows:
```
pip install pipenv
pipenv install
```
<p>for other os use this <a href="https://pypi.org/project/pipenv/#installation">documentation</a> to install pipenv. </p>

## Configuration
create database
```
CREATE DATABASE yourdatabasename;
```
add .env file
```
DB_NAME = yourdatabasename
DB_USER = yourusername
DB_PASSWORD = yourpassword
DB_HOST = yourdatabasehost
DB_PORT = yourdatabaseport
SECRET_KEY = yoursecretkey
```
```
cd CommunityCare
python manage.py migrate
python manage.py runserver
```

