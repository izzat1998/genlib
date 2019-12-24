from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from book.models import Book, Genre, Author
from book.serializers import BookSerializer, GenreSerializer, AuthorSerializer


class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GenreAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class AuthorAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
