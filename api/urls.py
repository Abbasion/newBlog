from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.users, name='users'),
    path('posts/<int:pk>', views.users, name='user'),
]

 
    