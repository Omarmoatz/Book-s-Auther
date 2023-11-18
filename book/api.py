from rest_framework import generics, filters,status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


from .serializers import BookSerialezer , AutherSerialezer, ReviewSerlizer
from .models import Book, Auther , Review




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

class BookDetailAPI(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        book_serializer = BookSerialezer(book)
        reviews = Review.objects.filter(book=book)
        reviews_serializer = ReviewSerlizer(reviews, many=True)

        return Response({
            'book': book_serializer.data,
            'reviews': reviews_serializer.data,
        }, status=status.HTTP_200_OK)





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



class AuthorDetailAPI(APIView):
    def get(self, request, pk):
        try:
            author = Auther.objects.get(pk=pk)
        except Auther.DoesNotExist:
            return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

        Author_serializer = AutherSerialezer(author)
        books = Book.objects.filter(auther=author)
        books_serializer = BookSerialezer(books, many=True)

        return Response({
            'Author': Author_serializer.data,
            'books': books_serializer.data,
        }, status=status.HTTP_200_OK) 





