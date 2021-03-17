from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    is_active = models.BooleanField(default=False)
    bio = models.CharField(max_length=200, null=True)

    def save(self, **kwargs):
        self.full_clean()
        return super().save(**kwargs)
