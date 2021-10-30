from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Post,UserProfile

# Create your views here.

@login_required(login_url='/accounts/login')
def home_page(request):
    neighborhoods = Neighborhood.objects.all()

    title = 'Home'
    return render(request, 'index.html', {'neighborhoods':neighborhoods,'title':title})