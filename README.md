# Django-todo
A simple todo app built with django

![image](https://user-images.githubusercontent.com/58668238/134215924-f32ada4f-ee6d-45db-ad56-69fa9cc46e81.png)
### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
$ git clone https://github.com/Salavat-VR/django-todo-app.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
$ make make_migrations
```
or
```bash
$ python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
$ make migrate
```
or
```bash
$ python manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
$ python manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command
```bash
$ make run
```
or
```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000 for the App.
