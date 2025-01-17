# library/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    number_of_copies = models.IntegerField()

    def __str__(self):
        return self.title

class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    date_of_membership = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checked_out_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
