from django.db import models

# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=100, primary_key=True, unique=True)
    password_hash = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, default="basic")

    def __str__(self):
        return self.userid + " " + self.role
