from django.urls import path
from .views import BookList  
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter()
router.register(r'books', views.BookList, basename='book-list')

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]


