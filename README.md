# Good News Blog

Blog application built with Django & Python 3.

## Getting started
Clone the repository:
```sh
$ git clone <repository url>
```
install the requirements:

```sh
$ pip3 install -r requirements.txt
```
Create a user to for the admin site. Run the following command:

```python
$ python manage.py createsuperuser
```
This will prompt you to enter a username, email & password.

Once complete, start the development server with the command:
```python
$ python manage.py runserver
```
To add new posts, navigate to 127.0.0.1:8000/admin/ and login with the
credentials you created.

Once you have your posts ready, navigate to 127.0.0.1:8000/blog

#### FYI
To search for posts navigate to /blog/search
To view the feed navigate to /blog/feed
To view the sitemap navigate /sitemap.xml


