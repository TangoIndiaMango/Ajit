from .serializers import BookSerializer, BookListSerializer
from .models import Book, BookAuthor, BookSubject, Bookshelf, Language, Format
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Count, Q
from rest_framework import generics, filters
from .models import Author, Book, BookAuthor, BookBookshelf, BookLanguage, BookSubject, Bookshelf, Format
from .serializers import AuthorSerializer, BookSerializer, BookAuthorSerializer, BookBookshelfSerializer, BookLanguageSerializer, BookSubjectSerializer, BookshelfSerializer, FormatSerializer
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author, Language, Subject, Bookshelf, Format
from .serializers import BookSerializer

# class BookList(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         filter_criteria = self.request.query_params.get('filter_criteria', None)

#         if filter_criteria is not None:
#             for filter in filter_criteria.split(","):
#                 if "language" in filter:
#                     language = filter.split("=")[1]
#                     books = books.filter(language=language)
#                 elif "mime_type" in filter:
#                     mime_type = filter.split("=")[1]
#                     books = books.filter(mime_type=mime_type)
#                 elif "topic" in filter:
#                     topic = filter.split("=")[1]
#                     books = books.filter(Q(subjects__icontains=topic) | Q(bookshelves__icontains=topic))
#                 elif "author" in filter:
#                     author = filter.split("=")[1]
#                     books = books.filter(author__name__icontains=author)
#                 elif "title" in filter:
#                     title = filter.split("=")[1]
#                     books = books.filter(title__icontains=title)

#         books = books.order_by('-downloads')[:25]
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

# class BookDetail(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()

        # Filtering
        filters = request.query_params
        if filters:
            if 'id' in filters:
                books = books.filter(id__in=filters.getlist('id'))
            if 'language' in filters:
                books = books.filter(languages__in=filters.getlist('language'))
            if 'mime_type' in filters:
                books = books.filter(
                    formats__mime_type__in=filters.getlist('mime_type'))
            if 'topic' in filters:
                topic = filters.getlist('topic')[0]
                books = books.filter(Q(subjects__name__icontains=topic) | Q(
                    bookshelves__name__icontains=topic))
            if 'author' in filters:
                books = books.filter(
                    authors__name__in=filters.getlist('author'))
            if 'title' in filters:
                books = books.filter(title__icontains=filters.get('title'))

        # Sorting
        books = books.order_by('-download_count')

        # Pagination
        page = self.paginate_queryset(books)
        if page is not None:
            serializer = BookSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    # Serialization
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookAuthorList(generics.ListAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class BookAuthorDetail(generics.RetrieveAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class BookBookshelfList(generics.ListAPIView):
    queryset = BookBookshelf.objects.all()
    serializer_class = BookBookshelfSerializer


class BookBookshelfDetail(generics.RetrieveAPIView):
    queryset = BookBookshelf.objects.all()
    serializer_class = BookBookshelfSerializer


class BookLanguageList(generics.ListAPIView):
    queryset = BookLanguage.objects.all()
    serializer_class = BookLanguageSerializer


class BookLanguageDetail(generics.RetrieveAPIView):
    queryset = BookLanguage.objects.all()
    serializer_class = BookLanguageSerializer


class BookSubjectList(generics.ListAPIView):
    queryset = BookSubject.objects.all()
    serializer_class = BookSubjectSerializer


class BookSubjectDetail(generics.RetrieveAPIView):
    queryset = BookSubject.objects.all()
    serializer_class = BookSubjectSerializer


class BookshelfList(generics.ListAPIView):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer


class BookshelfDetail(generics.RetrieveAPIView):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer


class FormatList(generics.ListAPIView):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class FormatDetail(generics.RetrieveAPIView):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format)
    })


class BookPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        # get filter criteria from query params
        book_id = self.request.query_params.getlist('book_id')
        language = self.request.query_params.getlist('language')
        mime_type = self.request.query_params.getlist('mime_type')
        topic = self.request.query_params.getlist('topic')
        author = self.request.query_params.getlist('author')
        title = self.request.query_params.getlist('title')

        # apply filters
        if book_id:
            queryset = queryset.filter(id__in=book_id)
        if language:
            queryset = queryset.filter(language__code__in=language)
        if mime_type:
            queryset = queryset.filter(format__mime_type__in=mime_type)
        if topic:
            queryset = queryset.filter(
                Q(subject__name__in=topic) | Q(bookshelf__name__in=topic))
        if author:
            queryset = queryset.filter(author__name__in=author)
        if title:
            queryset = queryset.filter(title__icontains=title)

        # sort by download count
        queryset = queryset.order_by('-download_count')

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # apply pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # return all results if pagination is not applied
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.query_params.get('book_id') or self.request.query_params.get('title'):
            return BookSerializer
        return BookListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookAuthorList(generics.ListAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class BookAuthorDetail(generics.RetrieveAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class BookBookshelfList(generics.ListAPIView):
    queryset = BookBookshelf.objects.all()
    serializer_class = BookBookshelfSerializer


class BookBookshelfDetail(generics.RetrieveAPIView):
    queryset = BookBookshelf.objects.all()
    serializer_class = BookBookshelfSerializer


class BookLanguageList(generics.ListAPIView):
    queryset = BookLanguage.objects.all()
    serializer_class = BookLanguageSerializer


class BookLanguageDetail(generics.RetrieveAPIView):
    queryset = BookLanguage.objects.all()
    serializer_class = BookLanguageSerializer


class BookSubjectList(generics.ListAPIView):
    queryset = BookSubject.objects.all()
    serializer_class = BookSubjectSerializer


class BookSubjectDetail(generics.RetrieveAPIView):
    queryset = BookSubject.objects.all()
    serializer_class = BookSubjectSerializer


class BookshelfList(generics.ListAPIView):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer


class BookshelfDetail(generics.RetrieveAPIView):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer


class FormatList(generics.ListAPIView):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class FormatDetail(generics.RetrieveAPIView):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer
