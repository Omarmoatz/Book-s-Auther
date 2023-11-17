from django.urls import path
from book.api import BookListAPI,AutherListAPI,BookDetailAPI, AutherDetailAPI




urlpatterns = [
    path('api/list', BookListAPI.as_view() ),
    path('api/listt', AutherListAPI.as_view() ),
    path('api/detail/<int:pk>', BookDetailAPI.as_view() ),
    path('api/detaill/<int:pk>', AutherDetailAPI.as_view()),
]