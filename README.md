[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e9618003d5c04cfcb04995f539d9198a)](https://www.codacy.com/gh/BuildForSDGCohort2/Team-1053-backend?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BuildForSDGCohort2/Team-1053-backend&amp;utm_campaign=Badge_Grade) 

# About Application

> This is the code for the backend API built with Python Django Rest Framework. Live application is hosted [here](https://saleslogistists.web.app)

## Table of Contents

- [About Application](#about-application)
  - [Table of Contents](#table-of-contents)
  - [Tech Stack](#tech-stack)
  - [Installation](#installation)
    - [Clone](#clone)
    - [Setup](#setup)
  - [Features](#features)
  - [Tests](#tests-optional)
  - [Contributing](#contributing)
    - [Step 1](#step-1)
    - [Step 2](#step-2)
    - [Step 3](#step-3)
  - [Support](#support)
  - [License](#license)

---

## Tech Stack

- Python 3.8
- Django Rest Framework
- Heroku

---

## Installation

- All you need to get started

### Clone

- Clone this repo to your local machine using `https://github.com/BuildForSDGCohort2/Team-1053-backend.git`

### Setup

- This application is built using Python Django.
- Install latest Python 3.8 in computer using this link [Install Python 3.8.0](https://www.python.org/downloads/release/python-380/)
- Install a current version Django - [How to install Django](https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release).
- Django CLI depends on the current version of pip - [The Python Package Installer](https://pip.pypa.io/en/stable/).. To check that the pip installed, run the the following command in a terminal:

  > `pip -V`

- Python applications require Python environments. Within the root directory, Install [Virtualenv](https://virtualenv.pypa.io/en/latest/), create a virtual environment and activate if using the following command:

  > `$ pip install virtualenv`

  > `$ virtualenv venv`

  > `$ source venv/bin/activate`

- To install [Django REST framework](https://www.django-rest-framework.org/), run the following command in the terminal:

  > `$ pip install djangorestframework`

- Create a .env file and connect your database using the following environment variables: Smartg

```
  export SECRET_KEY=your secret key
  export DEBUG=False
  export DB_ENGINE=django.db.backends.postgresql
  export DB_NAME=your database name
  export DB_USER=your username
  export DB_PASSWORD=your password
  export DB_HOST=localhost
  export DB_PORT=your database port
  ```

- In the root directory, run the following command in the terminal to install the necessary packages:

  > `$ pip install -r requirements.txt`

- In the root directory, run database migrations using the command in the terminal:

  > `$ python manage.py migrate`

- To start the development server, run the following command in the terminal:
  > `$ python manage.py runserver`

## Features

### User Account

- User registration and login
- Update user profile
- Delete user account

### Admin dashboard

- Information about stock
- Information about customers
- Information about Products
- Information about customer Orders
- Add, edit, delete, and view stock
- Add, edit, delete, and view customers
- Add, edit, delete, and view Products
- Add, edit, delete, and view Orders

### Customer dashboard

- Information about customer Orders
- Add, edit, delete, and view Orders

### Products management

- Add, edit, delete, and view stock
- Add, edit, delete, and view tags
- Add, edit, delete, and view Products

### Order management

- Add, edit, delete, and view order items
- Add, edit, delete, and view orders

### Order tracking

- Track order history

## Tests

- To execute the test, run the following command in the terminal:
  `$ python manage.py test`

---

## Contributing

> To get started...

### Step 1

- **Option 1**

  - Fork this repo!

- **Option 2**
  - Clone this repo to your local machine using `https://github.com/BuildForSDGCohort2/Team-1053-backend.git`

### Step 2

- **HACK AWAY!**
  - Create a branch in your local machine and implement the feature.
  - Push the changes in your branch.

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/BuildForSDGCohort2/Team-1053-backend/compare/" target="_blank">`API`</a>.

---

## Support

Reach out to me at one of the following places!

- My Website at <a href="https://bonifaseorwa.com" target="_blank">`Bonifase Orwa`</a>
- Twitter at <a href="https://twitter.com/bonifaseorwa" target="_blank">`@bonifase`</a>

---

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

- **[Apache 2.0 License](https://opensource.org/licenses/Apache-2.0)**

- Copyright 2020 © By <a href="http://orwabonifase.com" target="_blank">Bonifase</a>.
