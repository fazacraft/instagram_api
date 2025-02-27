from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title', 'description', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data['title']
        author = data['author']

        if not title.isalpha():
            raise ValidationError({'status':False, 'message': 'title must be alphanumeric'})


        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({'status':False, 'message': 'book already exists'})

        return data
