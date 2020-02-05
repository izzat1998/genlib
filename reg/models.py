from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
from django.utils.text import slugify


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.first_name


