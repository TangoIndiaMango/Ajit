from rest_framework import serializers
from .models import Author, Book, BookAuthor, BookBookshelf, Language, Subject, BookLanguage, BookSubject, Bookshelf, Format


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year', 'death_year']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['id', 'name']


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['id', 'mime_type', 'url']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    languages = LanguageSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    bookshelves = BookshelfSerializer(many=True)
    formats = FormatSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'languages', 'subjects',
                  'bookshelves', 'formats', 'download_count', 'gutenberg_id', 'media_type']


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ['id', 'book', 'author']


class BookBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBookshelf
        fields = ['id', 'book', 'bookshelf_id']


class BookLanguageSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()

    class Meta:
        model = BookLanguage
        fields = ['id', 'book', 'language']


class BookSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubject
        fields = ['id', 'book', 'subject_id']


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['id', 'name']


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['id', 'mime_type', 'url', 'book']

from rest_framework import serializers
from .models import Author, Book, Language, Subject, Bookshelf, Format


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year', 'death_year']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['id', 'name']


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['id', 'mime_type', 'url']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    bookshelves = BookshelfSerializer(many=True, read_only=True)
    formats = FormatSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'languages', 'subjects', 'bookshelves', 'formats']


class BookListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    bookshelves = BookshelfSerializer(many=True, read_only=True)
    formats = FormatSerializer(many=True, read_only=True)
    download_count = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'languages', 'subjects', 'bookshelves', 'formats', 'download_count']
