from django.contrib import admin

from .models import Author, Book, BookAuthor, BookBookshelf, BookLanguage,Language, BookSubject, Bookshelf, Format

# Register your models here.
admin.site.register((Author, Book, BookAuthor, BookBookshelf, BookLanguage, Language, BookSubject, Bookshelf, Format, ))