from django.test import TestCase
from django.core.exceptions import ValidationError

from blog.models import Post, Comment


class PostModelTest(TestCase):

    def setUp(self):
        self.year = '2017'
        self.month = '06'
        self.day = ''

        self.a_post = Post()

    def test_str_representation(self):
        """test that a blog post title's string representation is equal to it's title"""
        post = Post(title='My post title')
        self.assertEqual(str(post), post.title)

   def test_get_absolute_url(self):
        self.assertEqual('/blog/post_detail/', self.test_get_absolute_url())


class TestModelMeta(TestCase):

    def test_post_model_data(self):
        self.assertEqual(('-publish',), Post()._meta.ordering)

    def test_comment_model_data(self):
        self.assertEqual(('created',), Comment()._meta.ordering)



