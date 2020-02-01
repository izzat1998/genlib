from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from book.models import Book, Genre, Author


class Index(View):
    def get(self, request):
        return render(request, 'custom_admin/dashboard.html')


class Books(View):
    def get(self, request):
        book_list = Book.objects.all()
        context = {"book_list": book_list}
        return render(request, 'custom_admin/book/books.html', context=context)


class BookUpdate(View):
    def get(self, request, id):
        selected_book = Book.objects.get(id=id)
        context = {"book": selected_book}
        return render(request, 'custom_admin/book/book_update.html', context=context)

    def post(self, request, id):
        name = request.POST.get('book_name')
        description = request.POST.get('book_description')
        image = request.FILES['book_image']
        file = request.FILES['book_file']
        book = Book.objects.get(id=id)
        book.name = name
        book.description = description
        book.image = image
        book.file = file
        book.save()
        return HttpResponseRedirect(reverse('books'))


class Genres(View):
    def get(self, request):
        genre_list = Genre.objects.all()
        context = {"genre_list": genre_list}
        return render(request, 'custom_admin/genre/genres.html', context=context)


class GenreUpdate(View):
    def get(self, reqeust, id):
        selected_genre = Genre.objects.get(id=id)
        context = {'genre': selected_genre}
        return render(reqeust, 'custom_admin/genre/genre_update.html', context=context)


class Authors(View):
    def get(self, request):
        author_list = Author.objects.all()
        context = {"author_list": author_list}
        return render(request, 'custom_admin/author/authors.html', context=context)


class AuthorUpdate(View):
    def get(self, request, id):
        selected_author = Author.objects.get(id=id)
        context = {'author': selected_author}
        return render(request, 'custom_admin/author/author_update.html', context=context)
