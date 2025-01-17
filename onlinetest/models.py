from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Question(models.Model):
    title = models.CharField(max_length=1024)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        str_repr = self.text[:51] + \
            "..." if (len(self.text) >= 52) else self.text
        return str_repr


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_left = models.IntegerField(default=3600) #time in seconds, default 1hour
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    rollno = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name
