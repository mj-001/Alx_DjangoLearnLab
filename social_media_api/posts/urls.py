from django.urls import path 
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import CommentViewSet
from .views import FeedView

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
]
