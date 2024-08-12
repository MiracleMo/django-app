# A Simple toDo app to train my knowledge.

## Description
This is a simple web applicatioin in Django to understand and practice tools like Docker, VSCode and Git. Bulma CSS is used for the style of the app. 

## Run App
### Run App via Docker
- Start Docker
- In the directory of the project, run the command "docker compose up"
- If you want to use VSCode:
  1. Attach to the container named django-app with the Remote development extension pack
  2. In the new VSCode window applie migrations with "python manage.py makemigrations" and "python manage.py migrate"
  3. Run the app with "python manage.py runserver 0.0.0.0:8000"
  4. Connect to the app in any browser with either 127.0.0.1:8000 or localhost:8000
- Instead of VSCode you can open the container in docker and run the commands the exec tab
