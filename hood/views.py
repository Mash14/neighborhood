from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Post,UserProfile

# Create your views here.

@login_required(login_url='/accounts/login')
def home_page(request):
    posts = Post.objects.order_by('-title')

    title = 'Home'
    return render(request, 'index.html', {'posts':posts,'title':title})