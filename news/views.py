from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class PoliticPageView(ListView):
    model = Post   
    template_name = 'politics.html'

class NewsDetailView(DetailView):  
    model = Post
    template_name = 'news_detail.html'  