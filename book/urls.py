from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from book.views import BookAPIView, GenreAPIView, AuthorAPIView, GenreDetailAPIView, BookDetailAPIView, \
    AuthorDetailAPIView

urlpatterns = [
    #                   List
    path('book/list/', BookAPIView.as_view(), name='book-list'),
    path('genre/list/', GenreAPIView.as_view(), name='genre-list'),
    path('author/list/', AuthorAPIView.as_view(), name='author-list'),
    #                   Detail
    path('book/detail/<int:id>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('genre/detail/<int:id>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('author/detail/<int:id>/', AuthorDetailAPIView.as_view(), name='author-detail'),
]
