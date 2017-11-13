# milo_django_task

A simple web application to manage extended User model and export it to CSV

Functionality:
* adding, deleting, editing users and viewing user details
* custom filtering based on birthday and number
### Task
https://we.tl/ijbi4SLpR3
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
### Prerequisites
You need to have Python 3.5.3 at least, pip and virtualenv to run this project properly.

To install pip if you don't have one:
```
$ python get-pip.py
```
To install virtualenv:
```
$ pip install virualenv
```
### Installing
1) Clone thee project:
```
$ git clone https://github.com/AnastasiaMazur/milo_django_task.git
```
2) Create and run virtualenv:
```
$ virtualenv -p python3 env
$ source env/bin/activate
```
3) Open the project folder and install all requirements needed via pip:
```
cd milo_django_task && pip install requirements.txt
```
4) Create migration files based on your models and create the tables in your db based on the migration files created
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5) Run project (be sure that 8000 port is free):
```
$ python manage.py runserver
```
6) To see all the functionality, you should add a couple of users by
```
$ django-admin createsuperuser
```
or just add them in running project by clicking 'Add User' button
## Versioning
Using Python 3.5.3 & Django 1.11.5
### Authors
* **Anastasia Mazur**
