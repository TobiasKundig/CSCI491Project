from django.db import models
from django.conf import settings


class Portfolio(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    header = models.CharField(max_length=150)
    style = models.CharField(max_length=30)
    img = models.ImageField(default=None,verbose_name='main')

class ImageContent(models.Model):
    image = models.ImageField(default=None)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

class TextContent(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField()
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length =30)
    content = models.CharField(max_length=400)
    date = models.DateField()
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)