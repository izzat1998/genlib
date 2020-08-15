from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import BookViewSet, AuthorViewSet, GenreCRUDViewSet, MainPageBooks

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'genre', GenreCRUDViewSet, basename='genre')

urlpatterns = [
    path('main_page/books/', MainPageBooks.as_view(), name='main-page')
]
urlpatterns += router.urls
