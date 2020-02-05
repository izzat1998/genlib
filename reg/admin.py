from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from reg.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'phone_number', 'email']
    pass


admin.site.register(CustomUser, UserAdmin)
