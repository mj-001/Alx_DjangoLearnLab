from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# Create your views here.

class BookListView(generics.ListAPIView):
    """
    Handles listing all Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for all


class BookDetailView(generics.RetrieveAPIView):
    """
    Handles retrieving a single Book instance by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for all


class BookCreateView(generics.CreateAPIView):
    """
    Handles creating a new Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        """
        Customize the creation of a book.
        """
        serializer.save()  # Add logic here if needed


class BookUpdateView(generics.UpdateAPIView):
    """
    Handles updating an existing Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

    def perform_update(self, serializer):
        """
        Customize the update of a book.
        """
        serializer.save()  # Add logic here if needed


class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deleting a Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete
