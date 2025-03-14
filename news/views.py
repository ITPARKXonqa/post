from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Category


# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'categories'
    
    
    def get_queryset(self):
        categories = Category.objects.all()
        data = []
        for category in categories:
            posts = Post.objects.filter(category=category).order_by('-created_at')[:5]
            data.append({'category': category, 'posts': posts})
        return data 
        # return  Post.objects.order_by('-created_at')[:5]
    
    
class CategoryPageListView(ListView):
    model = Post   
    template_name = 'news.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return Post.objects.filter(category=category)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        return context

class NewsDetailView(DetailView):  
    model = Post
    template_name = 'news_detail.html'  

class LoginPageView(TemplateView):
    template_name = 'login.html'   
   
class RegisterPageView(TemplateView):
    template_name = 'register.html'       