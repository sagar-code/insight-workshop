from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table: "profile_info"

