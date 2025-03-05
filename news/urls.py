from django.urls import path
from .views import HomePageView, PoliticPageView, NewsDetailView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('politics/', PoliticPageView.as_view(), name='politics'),
    path('news_detail/<int:pk>',NewsDetailView.as_view(), name='news_detail')
]