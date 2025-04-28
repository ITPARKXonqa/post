from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    HomePageView, 
    CategoryPageListView, 
    NewsDetailView, 
    RegisterView,
    CustomLoginView,
    CustomLogoutView
    )

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('category/<slug:slug>', CategoryPageListView.as_view(), name='category_posts'),
    path('news_detail/<int:pk>',NewsDetailView.as_view(), name='news_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
]

# Media fayllarni developmentda ko'rsatish uchun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)