from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    username = models.CharField(max_length=100)
    course = models.ManyToManyField('Course', 'users')


class Course(models.Model):
    name = models.CharField(max_length=250)


class Tags(models.Model):
    name = models.CharField(max_length=200)
