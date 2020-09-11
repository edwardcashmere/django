# Django Project

Assets include:-

* django
* django-crispy-forms

## Project Set-Up
when initializing a new project in django
``` bash
pipenv shell 

```

this will create a new a virtual environment.Type exit on the bash shell to exit the virtual environment and pipenv shell when working on the project every time.

Next run 
```bash
pipenv install django

```
to intsall django when done run:-

```bash
django admin startproject **project name**
```
This will create a new project in your current directory.If you check your project you will notice that a new folder with your project name will have been created.when you cd into the folder you will notice 2files and a folder inside, a manage.py file ,another folder with the projectname but inside it contains the project set-up and configs ,you will mainly edit the settings.py and urls.py files.the last is the default database which is db.sqlite. 
run the following coomand to make sure the project is working.

```bash 
python manage.py runserver

```
after go to *localhost:8000* and you should see the default django page being serve here.It should as below

![django default page](https://i.stack.imgur.com/MzXfs.png)


## Application Set-up
From here onwards we will be creating apps for the different services we want our application to be handling,the way django works, we can have an app for the different services e.g a service to handle user login and registration a service for handling posts etc...
To create the first app run the following commands.

```bash
python manage.py startapp 'app-name'

```

replace the app-name with the desired app-name.After running this you will notice a new folder created with your app-name.If you cd into the folder you should find the folowing files:-

* \__init__.py *this should be empty normally*
* admin.py 
* app.py 
* models.py  
* tests.py 
* urls.py
* views.py

After you create the app the first thing to do is register it in the settings.py file 



