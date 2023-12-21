from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list),
    path('search/', search_books, name='search_books'),
    path('create/', create_book,),
    path('<int:id>/', book_detail),
]