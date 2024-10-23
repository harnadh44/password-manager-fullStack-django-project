from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.website_name
