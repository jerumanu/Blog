{% if False %}

# Introduction

The goal of this project is to provide  users to post blog , edit  blog and to read blog post by other users .

BLOG APP is written with django 4.o.5 and python 3.10 in mind.

### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Procfile for easy deployments

* Separated requirements files

* Postgresql for database

# Usage

For users to read an  post blog

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    pip install django

And then run the `django-admin` command to start the new project:

    $ django-admin startproject . \
      --Blog app=https://github.com/jerumanu/Blog.git \
      --extension=py,md \
      <blog>

### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    pip3 install django

And then:

    $ python3 -m django startproject \
      ----Blog-app =https://github.com/jerumanu/Blog.git \
      --extension=py,md \
      <blog >

After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ Blog App|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    git clone https://github.com/jerumanu/Blog.git \
    cd {{ BLOG }}

Activate the virtualenv for your project.

Install project dependencies:

    pip install -r requirements.txt

Then simply apply the migrations:

    python manage.py migrate

You can now run the development server:

    python manage.py runserver
