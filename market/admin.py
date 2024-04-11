from django.contrib import admin

from market.models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author']
    list_display = ['name', 'author', 'price', 'page_count', 'category']
    list_filter = ['category']
    list_editable = ['price']
    list_per_page = 10


admin.site.register(Book, BookAdmin)
