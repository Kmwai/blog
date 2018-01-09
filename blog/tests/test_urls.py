from django.test import TestCase
from django.core.urlresolvers import resolve
from blog.views import post_list


class SolosURLsTestCase(TestCase):

    # def test_root_url_uses_index_view(self):
     #   """Test the root of the site resolves to the main function"""
     #   root = resolve('/')
     #   self.assertEqual(root.func, post_list)

    def test_blog_solo_details_url(self):
        """

        :return:
        """
        blog_detail = resolve('/blog/2017/11/16/i-would-have-been-perfectly-submissive/')

        self.assertEqual(blog_detail.func.__name__, 'post_detail')
        self.assertEqual(blog_detail.kwargs['year'], '2017')
        self.assertEqual(blog_detail.kwargs['month'], '11')
        self.assertEqual(blog_detail.kwargs['day'], '16')
        self.assertEqual(blog_detail.kwargs['post'], 'i-would-have-been-perfectly-submissive')