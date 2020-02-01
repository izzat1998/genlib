from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import Index, Books, Authors, Genres, BookUpdate, GenreUpdate, AuthorUpdate

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('books/', Books.as_view(), name='books'),
    path('book/<int:id>/', BookUpdate.as_view(), name='book-update'),
    path('genres/', Genres.as_view(), name='genres'),
    path('genre/<int:id>/', GenreUpdate.as_view(), name='genre-update'),
    path('authors/', Authors.as_view(), name='authors'),
    path('author/<int:id>/', AuthorUpdate.as_view(), name='author-update'),

]
