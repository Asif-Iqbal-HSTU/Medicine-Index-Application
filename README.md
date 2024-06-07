# Project Setup Guide
## Installation
### Clone the repository:
  ```bash
  git clone https://github.com/Asif-Iqbal-HSTU/Medicine-Index-Application
  ```
  ```bash
  cd Medicine-Index-Application
  ```
### Set Up a Virtual Environment:
  ```bash
  python -m venv venv
  ```
  
  ```bash
  venv\Scripts\activate
  ```
### Install Dependencies:
  ```bash
  pip install -r requirements.txt
  ```
### Apply Migrations:
  ```bash
  python manage.py migrate
  ```
### Collect Static Files
  ```bash
  python manage.py collectstatic
  ```
### Run the Development Server:
  ```bash
  python manage.py runserver
  ```
### Visit on browser:
  ```bash
  127.0.0.1:8000
  ```
