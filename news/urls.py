from django.urls import path
from .views import (
    HomePageView, 
    PoliticPageView, 
    NewsDetailView, 
    LoginPageView, 
    RegisterPageView
    )

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('politics/', PoliticPageView.as_view(), name='politics'),
    path('news_detail/<int:pk>',NewsDetailView.as_view(), name='news_detail'),
    path('login/',LoginPageView.as_view(), name='login'),
    path('register/',RegisterPageView.as_view(), name='register')
]