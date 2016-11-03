from django.db import models
from django.conf import settings


class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    header = models.CharField(max_length=60)
    style = models.CharField(max_length=30)
    stylesheet = models.CharField(max_length=100)
    frontpage = models.BooleanField(default=False)

class Content(models.Model):
    text = models.CharField(max_length=400)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

class Photos(models.Model):
    title = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    dimX = models.IntegerField(default=400)
    dimY = models.IntegerField(default=300)
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