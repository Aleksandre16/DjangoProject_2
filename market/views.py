from django.http import JsonResponse

from market.models import Book
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


def get_books(request):
    books = Book.objects.all()
    return JsonResponse({'books': list(books.values())})


def get_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        return JsonResponse({'book': {
            'name': book.name,
            'author': book.author,
            'price': book.price,
            'page_count': book.page_count,
            'category': book.category,
            'image': book.image.url if book.image else None, }})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)


def get_listedbooks(request):
    books = Book.objects.all()
    paginator = Paginator(books, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books.html', {'page_obj': page_obj})


def book_detail(request, book_id):
    # Retrieve the book object using the book_id
    book = get_object_or_404(Book, id=book_id)

    # Render the book detail template with the book object
    return render(request, 'book_detail.html', {'book': book})
