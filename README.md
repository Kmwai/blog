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

```sh
$ python manage.py createsuperuser
```
This will prompt you to enter a username, email & password.

Once complete, start the development server with the command:
```sh
$ python manage.py runserver
```
To add new posts, navigate to <span style="color:blue">127.0.0.1:8000/admin/</span> and login with the
credentials you created.

Once you have your posts ready, navigate to <span style="color:blue">127.0.0.1:8000/blog</span>

#### FYI
* To search for posts navigate to <span style="color:blue">/blog/search</span>
* To view the feed navigate to <span style="color:blue">/blog/feed</span>
* To view the sitemap navigate <span style="color:blue">/sitemap.xml</span>


[Click here for demo](https://good-news-blog.herokuapp.com)

