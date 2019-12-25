from abc import ABC

from rest_framework import serializers

from book.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name_en', 'name_ru']


class BookSerializer(serializers.ModelSerializer, ):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'genre', 'name', 'description', 'image', 'file', 'author']


class BookSerializerWithoutGenre(serializers.ModelSerializer, ):
    author = AuthorSerializer

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'image', 'file', 'author']


class BookSerializerWithoutAuthor(serializers.ModelSerializer, ):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'genre', 'name', 'description', 'image', 'file']
