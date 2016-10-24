from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=30)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Portfolio(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
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