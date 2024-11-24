from django.shortcuts import render
from rest_framework.generics import generics.ListAPIView
from .serializers import BookSerializer
from .models import Book

class BookList(ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  


