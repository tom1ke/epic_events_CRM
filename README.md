# Epic Events
CRM system built with Django & Django Rest Framework

Version : Python 3.10.1

 ## Django project setup
- Clone the repository with ```$ git clone https://github.com/tom1ke/epic_events_CRM.git```
- Go to project root directory in a terminal
- Create a virtual environment with

  - MacOS / Linux ```$ python3 -m venv env```

  - Windows ```$ python -m venv env```
- Activate the virtual environment with

  - MacOS / Linux ```$ source env/bin/activate```

  - Windows ```$ env\Scripts\activate```
- Install project dependencies with ```$ pip install -r requirements.txt```
- Go to Django project directory with ```$ cd src```
- Setup the database (cf. 'Database setup' below)
- Run local server with ```$ python manage.py runserver```
- Access the API with a web browser or Postman type tool at : http://127.0.0.1:8000/

Those steps are valid for initial setup. For further use, juste activate the virtual environment and run the server.

## Database setup
This application uses a PostgreSQL database. You can create your own database and connect it to the application.

- Create your PostgreSQL database (with 'localhost' as host and '5432' as port)
- Open *src/src/settings.py*
- Look for ```DATABASES``` and change the value of
    - ```'NAME'``` with your database name
    - ```'USER'```with your database user
- Save changes
- Run ```$ python manage.py makemigrations```
- Run ```$ python manage.py migrate```

## Documentation
The API and endpoints documentation is available on Postman :

https://documenter.getpostman.com/view/19593831/2s83KRiRxw


## Authentication
Authentication works with a bearer token system (JWT). You must have a account created by an administrator in order to use the API.

You will find the endpoints and information related to authentication in the Postman documentation.

## Administration
To access Django administration interface you must create a *superuser* profile.
Afin d'accéder à l'interface d'administration de l'API il est nécessaire de créer un profil de *superuser*.

To do it, go to Django project directory with a terminal, use ```$ python manage.py createsuperuser``` and follow the instructions.

You can now log in the administration interface with your newly created credentials at : http://127.0.0.1:8000/admin/