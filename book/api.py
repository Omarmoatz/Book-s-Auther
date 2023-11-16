from rest_framework import generics, filters

from .serializers import BookSerialezer , AutherSerialezer
from .models import Book, Auther

class BookListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialezer



class AutherListAPI(generics.ListCreateAPIView):
    queryset = Auther.objects.all()
    serializer_class = AutherSerialezer