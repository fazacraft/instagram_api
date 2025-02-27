from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=30,decimal_places=2, )


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title