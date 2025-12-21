from django.db import models

class Users(models.Model):
    nickname = models.CharField(max_length=16)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    token = models.CharField(max_length=100)

class Servers(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)