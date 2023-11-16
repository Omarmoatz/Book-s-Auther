from rest_framework import serializers
from .models import Book, Auther

class BookSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AutherSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = '__all__'