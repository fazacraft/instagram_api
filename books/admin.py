from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at', 'updated_at')