# blog

Simple blog application using Django

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

#### Important to note | class-based views
We can define views as class methods since a view is a callable that takes a web request 
and returns a web response. Using class based views is an alternate method to create your views.

In our case the class-based view used is analogous to the previous *post_list* view. 

if you decide to use the class-based view you can comment out the class-based view url in the blog/urls.py file:
```python
urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'), # url for class-based view
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]
```
Also, to keep pagination working, you have to use the right page object passed to the template(*post_list.html*)
We have to include the paginator using the variable *page_obj* as shown:
```python
{%  include "pagination.html" with page=page_obj %}
```