from django.db.models import Q
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book, Genre, Author
from book.serializers import BookSerializer, GenreSerializer, AuthorSerializer, BookSerializerWithoutGenre


class GenreCRUDViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        genre = self.request.GET.get('genre')
        author = self.request.GET.get('author')
        books = Book.objects.all()
        if genre is not None:
            books = books.filter(Q(genre__name_en__icontains=genre) | Q(genre__name_ru__icontains=genre)).distinct()
            return books
        if author is not None:
            books = books.filter(Q(author__name__icontains=author))
            return books
        return books


class MainPageBooks(APIView):
    def get(self, request):
        data = []
        books = Book.objects.all()[:10]
        for book in books:
            if book.image:
                detail = {'name': book.name,
                          'author': book.author.name,
                          'image': book.image_absolute_url}
            else:
                detail = {'name': book.name,
                          'author': book.author.name,
                          'image': 'No'}
            data.append(detail)

        return Response(data)
