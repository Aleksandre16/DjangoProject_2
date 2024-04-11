from django.urls import path

from market.views import get_books, get_book, get_listedbooks, book_detail

urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('books/<int:book_id>/', get_book, name='get_book'),
    path('books/listed/', get_listedbooks, name='get_listedbooks'),
    path('books/detail/<int:book_id>/', book_detail, name='book_detail'),

]

