from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('donate/food/', views.food_donate, name='food_donate'),
    path('donate/blood/', views.blood_donate, name='blood_donate'),
    path('donate/clothes/', views.clothes_donate, name='clothes_donate'),
    path('donate/books/', views.books_donate, name='books_donate'),
]
