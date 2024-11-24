from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specify the model the serializer is for
        fields = '__all__'  # Include all fields of the Book model
