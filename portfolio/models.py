from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=30)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    header = models.CharField(max_length=60)
    style = models.CharField(max_length=30)
    stylesheet = models.CharField(max_length=100)


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