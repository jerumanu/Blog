# Blog

## Author
* By Emmanuel Cheriyot 

## Description
This is web application that allow usesrs to view and post blog  delete blog taht does not impress other users

## Feature
* User is able to sign up and login the application
* User is able to view different blogs 
* User can create or upload blog
* Create blog that will be visible to everyon
*  User can delete or update  blog
## Behaviour Driven Development
| Input | Output|
|-------| ------|
| User sign up to create ,ubdate , delete and view thier own posted  blog 
| Users sees the posted  blog

## Setup and Installations

* Get the project
- Clone this repository
   

* Install and activate Virtual
- python3 -m venv virtual
- source virtual/bin/activate

* Navigate into the folder
- cd  Blog

* Install Dependencies
- pip install -r requirements.txt

* Setup Database
    - SetUp your database User,Password, Host then make migrations:
    - python manage.py makemigrations
    - python manage.py migrate

* Run application
    - python manage.py runserver

* Testing the application
    - python manage.py test

## Technology Used

* Python3.10
* Django 3.2.1
* Heroku

## Known Bugs
* There are no known bugs at the moment


## Copyright and License

The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2022.All rigths reserved
