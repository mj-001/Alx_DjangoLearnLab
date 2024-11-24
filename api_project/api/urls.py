from django.urls import path
from .views import BookList  
from rest_framework.routers import DefaultRouter
from . import views 

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Note: Correct 'urlpatterns'
]

router = DefaultRouter()
router.register(r'books', views.BookList, basename='book-list')
