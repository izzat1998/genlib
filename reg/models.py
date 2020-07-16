import datetime
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
from django.utils.text import slugify


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.username = self.email


class SecurityNumber(models.Model):
    secure_number = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(minutes=5))

    class Meta:
        db_table = 'security_number'

    def __str__(self):
        return str(self.secure_number)
