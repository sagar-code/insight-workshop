from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)


class UserDetail(models.Model):
    age = models.IntegerField()
    # one to one relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)