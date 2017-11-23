from django.test import TestCase

from blog.models import Post, Comment


class PostModelTest(TestCase):

    def test_str_representation(self):
        """test that a blog post title's string representation is equal to it's title"""
        post = Post(title='My post title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        post = Post.published.all(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/post/1')

