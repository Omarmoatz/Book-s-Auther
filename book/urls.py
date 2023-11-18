from django.urls import path
from book.api import BookListAPI,AutherListAPI,BookDetailAPI, AutherDetailAPI,BookDetailAPI,AuthorDetailAPI




urlpatterns = [
    path('api/list', BookListAPI.as_view() ),
    path('api/listt', AutherListAPI.as_view() ),
    path('api/detail/<int:pk>', BookDetailAPI.as_view() ),
    path('api/detaill/<int:pk>', AutherDetailAPI.as_view()),

    path('api/bookReview/<int:pk>', BookDetailAPI.as_view()),
    path('api/autherBook/<int:pk>', AuthorDetailAPI.as_view()),

    # path('<int:book_id>/reviews/', book_reviews, name='book_reviews'),
    # path('<int:book_id>/author/', book_author, name='book_author'),
]