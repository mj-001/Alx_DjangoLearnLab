from django.urls import path, include
from registration import views as reg_views

urlpatterns = [
    path('login/', include('django.contrib.auth.urls')),  # Built-in login/logout views
    path('register/', reg_views.register, name='register'),
    path('profile/', reg_views.profile_view, name='profile'),
]
