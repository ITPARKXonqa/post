from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post, Category

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


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
        return context

class NewsDetailView(DetailView):  
    model = Post
    template_name = 'news_detail.html'  
    context_object_name = 'post'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        categories = Category.objects.all()
        data = []
        for category in categories:
            posts = Post.objects.filter(category=category).all()
            data.append({'category': category, 'post_len': len(posts)})
        context['post_lens'] = data
        return context

# Ro'yxatdan o'tish uchun view
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

# Tizimga kirish uchun view
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Tizimdan chiqish uchun view
class CustomLogoutView(LogoutView):
    next_page = '/'
    
@login_required
def news_list(request):
    # Yangiliklarni chiqarish logikasi
    return render(request, 'home.html')    
