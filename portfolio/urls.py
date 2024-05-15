from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.portfolio_list, name="portfolio_list"),
    path('portfolio/<int:pk>/', views.portfolio_detail, name = 'portfolio_detail'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register"),
    path('portfolio/<int:pk>/likes/', views.portfolio_likes, name="portfolio_likes"),
]