from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import BookSerialezer , AutherSerialezer
from .models import Book, Auther

class BookListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialezer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title',]
    ordering_fields = ['price', 'publication_date']
    filterset_fields = ['price', 'publication_date']


class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialezer    




class AutherListAPI(generics.ListCreateAPIView):
    queryset = Auther.objects.all()
    serializer_class = AutherSerialezer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name',]
    ordering_fields = ['birth_date',]
    filterset_fields = ['name', 'biography']

class AutherDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auther.objects.all()
    serializer_class = AutherSerialezer