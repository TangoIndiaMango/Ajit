from django.urls import path
from .views import BookList, BookDetail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="API for managing books",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@bookapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    # path('authors/', AuthorList.as_view(), name='author-list'),
    # path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    # path('bookshelves/', BookshelfList.as_view(), name='bookshelf-list'),
    # path('bookshelves/<int:pk>/', BookshelfDetail.as_view(), name='bookshelf-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
