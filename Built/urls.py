from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register_user'),
    path('view_users/', views.view_users, name='view_users'),
    path('update/<str:user_email>/', views.update_user, name='update_user'),
    path('delete/<str:user_email>/', views.delete_user, name='delete_user'),
]
