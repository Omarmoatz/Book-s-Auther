from django.db import models
from django.utils import timezone

class Auther(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(default=timezone.now)
    biography = models.TextField(max_length=1000) 

    def __str__(self):
        return self.name

class Book(models.Model):
    auther = models.ForeignKey('Auther', on_delete=models.CASCADE, related_name='books_auther')
    title = models.CharField(max_length=50)
    publication_date = models.DateField(default=timezone.now)
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.title
    

class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='books_review')
    reviewer_name = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    rating = models.PositiveIntegerField(help_text='enter the review from 1 to 5 only')

    def __str__(self):
        return self.reviewer_name

