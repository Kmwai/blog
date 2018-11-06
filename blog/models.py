from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator, validate_email, RegexValidator, validate_slug
from taggit.managers import TaggableManager


# add custom published manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    # post model

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish', validators=[validate_slug])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # default manager
    published = PublishedManager()  # custom published manager
    tags = TaggableManager()

    class Meta:
        ordering = '-publish',

    # canonical url for Post objects
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    def __str__(self):  # __unicode__ on python 2
        return self.title


class Comment(models.Model):
    # comment model

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20, validators=[MinLengthValidator(10), RegexValidator("^[A-Z][a-z]{1,}$")])
    email = models.EmailField(validators=[validate_email])
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = 'created',

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)