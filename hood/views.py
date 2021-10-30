from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Post,UserProfile
from .forms import NeighborhoodForm,NewProfileForm

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

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    userProfile = UserProfile.objects.filter(user = current_user).first()
    title = 'Profile Page'
    return render(request, 'profile.html', {'userProfile':userProfile,'title':title})


@login_required(login_url='/accounts/login')
def update_profile(request):
    current_user = request.user
    userProfile = UserProfile.objects.filter(user = current_user).first()
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
            return redirect('profile_page')

    else:
        form = NewProfileForm()
        
    title = 'Update Profile'
    return render(request, 'update_profile.html',{'form':form,'title':title,'userProfile':userProfile})
