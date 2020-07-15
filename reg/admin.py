from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from reg.models import CustomUser, SecurityNumber


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'phone_number', 'email']


class UserSecureNumberAdmin(admin.ModelAdmin):
    list_display = ['secure_number', 'email', 'created_at', 'expiration_date']


admin.site.register(CustomUser, UserAdmin)
admin.site.register(SecurityNumber, UserSecureNumberAdmin)
