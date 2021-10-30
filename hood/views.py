from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Post,UserProfile
from .forms import NeighborhoodForm

# Create your views here.

@login_required(login_url='/accounts/login')
def home_page(request):
    neighborhoods = Neighborhood.objects.all()

    title = 'Home'
    return render(request, 'index.html', {'neighborhoods':neighborhoods,'title':title})

@login_required(login_url='/accounts/login')
def post_neighborhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST,request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit = False)
            neighborhood.user = current_user
            neighborhood.save()
        return redirect('home')
    else:
        form = NeighborhoodForm()

    title = 'Upload Neighborhood'
    return render(request, 'post_neighborhood.html',{'form':form,'title':title})
