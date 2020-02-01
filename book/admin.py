from django.contrib import admin

# Register your models here.
from book.models import Book, Author, Genre

admin.site.register(Genre)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ('name', 'description', 'image', 'file', 'created')
    list_filter = ('name',)
