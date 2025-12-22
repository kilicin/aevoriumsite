from django.db import models

class Users(models.Model):
    nickname = models.CharField(max_length=16)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    token = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nickname}'

class Servers(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'

class Donation(models.Model):
    name = models.CharField(max_length=16)
    mini_description = models.CharField(max_length=1000)
    description = models.CharField(max_length=100)
    server = models.ForeignKey(Servers, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.server} - {self.name}'

class Balances(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    server = models.ForeignKey(Servers, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.server} - {self.user}: {self.amount}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'server'], name='unique_user_server')
        ]

class Profile(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    donateBalance = models.IntegerField()

    def __str__(self):
        return f'{self.name}'