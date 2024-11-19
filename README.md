#STEPS TO RUN THIS PROJECT
#Open Any ide like pycharm or vs code
#Open folder You created for project
#Open terminal 
#Create virtual Environment
python -m venv Gam
#Activate your virtual Environment
Gam/scripts/activate #For Windows
#install django 
pip install Django-admin  #django-admin==specified_version 
#I used version is 5.1.3
#Python version 3.11.7
#Install MySQl client For external Database 
pip install mysqlclient  
#Create python project
django-admin startproject Gam   .
#Create python app name as Built
python manage.py startapp Built
#Run the Server once
#Create all necessary files and changes in app(Built) and project(Gam)
#Create templates and Static folders in Built app directoy 
#Inside templates folder place your html files
#Inside static folder place your css and js files
python manage.py collectstatic 
#Click on yes 
#Start your development server
python manage.py runserver
#Server start running localhost.. 
#Registration page will be displayed in localhost here we can perform Our CRUD operations
