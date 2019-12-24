from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
from django.utils.text import slugify


class CustomUser(AbstractUser):
    user_id = models.SlugField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.first_name

    def _get_unique_slug(self):
        slug = slugify(self.first_name + self.last_name)
        unique_slug = slug
        num = 1
        while CustomUser.objects.filter(user_id=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._get_unique_slug()
        super().save(*args, **kwargs)
