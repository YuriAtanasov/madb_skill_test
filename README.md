# Skillo Python and Django Final exam project

## Contents

- [Skillo Python and Django Final exam project](#skillo-python-and-django-final-exam-project)
  - [Contents](#contents)
  - [Planning](#planning)
  - [Repository structure](#repository-structure)
  - [Installation steps](#installation-steps)
    - [Prepare your PC environment](#prepare-your-pc-environment)
    - [Prepare Virtual Environment for project](#prepare-virtual-environment-for-project)
  - [Deactivate Virtual Environment for project](#deactivate-virtual-environment-for-project)
  - [Django project initial configuration](#django-project-initial-configuration)
    - [Run Django project](#run-django-project)
  - [Project resources used](#project-resources-used)

## Planning

Developing a movie application database with Django and Python can be a fun and educational project. Here's a broad outline of the steps you might follow:

1. **Planning the Application**: Before starting any project, it's crucial to plan out what the application will do, what features it will have, and how users will interact with it. For a movie application, you might want to include features like searching for movies, viewing detailed information about a movie, user authentication, user reviews, and ratings, etc.

2. **Setting Up the Environment**: Make sure Python, Django, and any other tools you need are installed and configured correctly on your computer. You may want to consider setting up a virtual environment using tools like `venv` or `pipenv`.

3. **Start the Django Project**: Start a new Django project using the `django-admin startproject` command.

4. **Create the Application**: Create a new Django app using the `python manage.py startapp` command.

5. **Design the Database Schema**: Design the database schema for your movie application. You'll need to consider what models you'll need (e.g., Movie, Actor, Genre, User, Review, etc.) and what fields each model will have. Django's ORM makes it easy to define these models and their relationships.

6. **Implement the Models**: Implement the database models in Django based on your schema.

7. **Create the Views**: Create the views for your application. These are the functions or classes that handle the requests from the user and return responses. In your case, you might have views for listing all movies, displaying a single movie, creating a new review, etc.

8. **Design and Implement the Templates**: Design and implement the HTML templates for your views. Django's template language makes it easy to insert dynamic data into your HTML.

9. **Implement User Authentication**: Django provides tools for user authentication out of the box, but you'll still need to create the views, forms, and templates for user registration, login, and logout.

10. **Test Your Application**: Write tests for your models, views, and other parts of your application to make sure everything works as expected. Django has a built-in testing framework that you can use.

11. **Deploy Your Application**: Once everything is working, you can deploy your application to a server so others can use it. There are many options for deploying Django applications, including Heroku, AWS, GCP, etc.

Throughout this process, you'll also need to consider other factors like how to structure your code, how to handle errors, how to make your application secure, etc. It's a good idea to read through the Django documentation and tutorials, which provide a lot of useful information on these topics.

Remember, building an application is an iterative process. Start with a simple version of your application, and add more features as you go along. Happy coding!

## Repository structure

```bash
└── madb (main repository)
   ├── madb_catalog (main Django project)
   |   ├── Docs
   |   |   └── README.md (initial implementation steps)
   |   |
   |   ├── madb_backend (Python backend)
   |   |   ├── migrations
   |   |   ├── static
   |   |   ├── templates
   |   |   |   ├── clients
   |   |   |   |   └── *.html (add form files)
   |   |   |   ├── movie_catalog
   |   |   |   |   ├── images
   |   |   |   |   |   └── movies
   |   |   |   |   |       └── *.jpg (movie db images)
   |   |   |   |   └── pages
   |   |   |   |       └── *.html (main app files)
   |   |   |   └── stats
   |   |   |       └── *.html (top-rated/most-watched-recently-added  movies)
   |   |   └── *.py (main app files)
   |   |
   |   ├── madb_catalog (Django frontend)
   |   |   └── *.py (Django frontend files)
   |   |
   |   ├── db.sqlite3 (Django database)
   |   ├── manage.py (Django project manager)
   |   └── README.md (project features and requirements)
   |
   ├── madbenv (virtual environment)
   ├── tools (scripts and tools)
   |   └── pip
   |       └── get-pip.py (pip installer)
   |
   ├── .gitignore (git ignore file)
   ├── README.md (this file)
   └── requirements.txt (project requirements)
```

## Installation steps

### Prepare your PC environment

- Install Python - [official website](https://www.python.org/downloads/)
  - Install pip (version 24.0)

    ```bash
    python3 ./tools/pip/get-pip.py
    #If file missing use: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
    ```

- Confirm installation

    ```bash
    pip3 --version
    pip --version
    ```

  - install Python and Django venv (python 3.10 & Django 5.3.0)

    ```bash
    cd ${repo_home}
    pip3 install virtualenv && \
    pip3 install django && \
    pip3 list
    ```

- install project requirements

    ```bash
    cd ${repo_home}
    pip3 install django -r requirements\ .txt
    ```

### Prepare Virtual Environment for project

- Once you're in the directory where you want to create the virtual environment, run the following command in your terminal:

  - On Unix or MacOS, run
    - cd ${repo_home}  

    ```bash
    python3 -m venv madbenv
    source madbenv/bin/activate
    ```

  - On Windows (with git client), run:
    - cd ${repo_home}

    ```bash
    py -3 -m venv madbenv
    source madbenv/Scripts/activate
    ```

- Now, your virtual environment is active, and you can start installing packages into it using `pip`. These packages will be isolated from your global Python environment.

## Deactivate Virtual Environment for project

- To deactivate the virtual environment and return to your global Python environment, simply run the following command:

    ```bash
        deactivate
    ```

## Django project initial configuration

> Ran once on initial project setup. !!! Not required !!!

- Created Django project and an app within the project named: `movie_app_database`
- Created Python backend named: movie_app_backend
- Repeat steps for "[Prepare your PC environment](#prepare-your-pc-environment)" and "[Prepare Virtual Environment for project](#prepare-virtual-environment-for-project)" sections

  - cd ${repo_home}

    ```bash
    django-admin startproject madb_catalog
    cd madb_catalog
    python manage.py startapp madb_backend
    ```

### Run Django project

- Perform the necessary migrations (initial step)
  - cd ${repo_home}/madb_catalog/

    ```bash
    python3 manage.py makemigrations && \
    python3 manage.py migrate
    ```

- On Unix or MacOS, run
  - cd ${repo_home}/madb_catalog

    ```bash
    python3 manage.py runserver
    ```

- On Windows (with git client), run:
  - cd ${repo_home}/madb_catalog

    ```bash
    python manage.py runserver
    ```

## Project resources used

- Python official page - [url](https://www.python.org/)
- Github Copilot - [url](https://github.com/features/copilot)
- Open AI ChatGPT - [url](https://platform.openai.com/)
- IMDB website - [url](https://www.imdb.com/)
