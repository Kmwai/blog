# blog

Blog application using Django

#### Implementation

First you need to create a user to manage your admin site. Run the following command

```sh
$ python manage.py createsuperuser
```
This will prompt you to enter a desired username, email & password

Now start the development server with the command:
```sh
$ python manage.py runserver
```
Then navigate to 127.0.0.1:8000/admin/ and login with the
credentials you used. Add new posts to the site as the models are already prepared.

Then navigate to 127.0.0.1:8000/blog/

