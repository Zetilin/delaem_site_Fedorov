from django.db import models

# Create your models here.

class User(models.Model):
    login = models.TextField()
    password = models.TextField()

    def __str__(self):
        return str(self.login)

class Tovar(models.Model):
    name=models.TextField()
    price=models.FloatField()

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    tovar_id = models.ForeignKey('Tovar', on_delete = models.CASCADE)