from django.urls import path 
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from . import views 

urlpatterns = [
    path("register/", views.RegisterUser.as_view()),
    path("login/", views.LoginUser.as_view()),
    path("logout/", TokenBlacklistView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("index", views.index, name = "index")
]