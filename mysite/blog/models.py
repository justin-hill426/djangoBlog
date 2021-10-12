from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    # This is the field for the post title. Translates to a VARCHAR column in the SQL DB
    title = models.CharField(max_length=250)
    # Intended to be used in URLs. Build beautiful, SEO-friendly URLs for blog posts
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # defines a one to many relationship, each post is written by a USER that can write any number of posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # This is the body of the post
    body = models.TextField()
    # When the post is published
    publish = models.DateTimeField(default=timezone.now())
    # Indicates when the post was created
    created = models.DateTimeField(auto_now_add=True)
    # Indicates the last time the post was updated
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title