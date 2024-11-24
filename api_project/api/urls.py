from django.urls import path
from .views import BookList  # Make sure this import is correct

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Note: Correct 'urlpatterns'
]
