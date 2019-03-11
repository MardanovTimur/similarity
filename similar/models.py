from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    username = models.CharField(max_length=100)
    course = models.ManyToManyField('Course', 'users')


class Course(models.Model):
    name = models.CharField(max_length=250)


class Tags(models.Model):
    name = models.CharField(max_length=200)


class MeraValue(models.Model):
    user_1 = models.ForeignKey(User, related_name='user_1_values', on_delete=models.CASCADE)
    user_2 = models.ForeignKey(User, related_name='user_2_values', on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        unique_together = (('user_1', 'user_2'),)
