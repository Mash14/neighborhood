from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Business, Neighborhood,Post,UserProfile,Police,Health
from .forms import NeighborhoodForm,NewProfileForm,NewBusinessForm,NewPostForm,UpdatePoliceForm,UpdateHealthForm

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

@login_required(login_url='/accounts/login')
def business(request):
    busines = Business.objects.all()

    title = 'Business'
    return render(request, 'business.html',{'business':busines,'title':title}) 

@login_required(login_url='/accounts/login')
def post_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.save()
            return redirect('business_list')
        
    else:
        form = NewBusinessForm()
    
    title = 'Post Business'
    return render(request,'post_business.html',{'form':form,'title':title})

@login_required(login_url='/accounts/login')
def single_business(request,id):
    business = Business.objects.get(id=id)

    title = 'Single Business'
    return render(request,'single_business.html',{'business':business,'title':title})

@login_required(login_url='/accounts/login')
def search(request):
    if 'name' in request.GET and request.GET['name']:
        search_term = request.GET.get('name')
        searched_business = Business.search_business(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'business':searched_business}) 

    else:
        message = "You haven't searched for any business, try again"
    
    return render(request, 'search.html', {'message': message})

@login_required(login_url='/accounts/login')
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('posts')

    else:
        form = NewPostForm()
    
    title = 'New Post'
    return render(request, 'create_post.html',{'form':form,'title':title})
        
@login_required(login_url='/accounts/login')
def posts_page(request):
    posts = Post.objects.order_by('-pub_date')

    title =  'Posts'
    return render(request, 'post.html',{'posts':posts,'title':title})

@login_required(login_url='/accounts/login')
def single_post(request,id):
    post = Post.objects.get(id = id)

    title = 'Single Post'
    return render(request, 'single_post.html',{'post':post,'title':title})

@login_required(login_url='/accounts/login')
def single_neighborhood(request,id):
    neighborhood = Neighborhood.objects.get(id = id)
    business = Business.objects.filter(neighborhood = neighborhood).all()
    posts = Post.objects.filter(neighborhood = neighborhood).all()
    police = Police.objects.filter(neighborhood=neighborhood).all()
    health = Health.objects.filter(neighborhood=neighborhood).all()

    title = 'Neighborhood'
    return render(request, 'single_neighborhood.html',{'neighborhood':neighborhood,'business':business,'posts':posts,'title':title,'police':police,'health':health})

@login_required(login_url='/accounts/login')
def post_police(request):
    if request.method == 'POST':
        form = UpdatePoliceForm(request.POST,request.FILES)
        if form.is_valid():
            center = form.save(commit=False)
            center.save()
            return redirect('home')
    
    else:
        form = UpdatePoliceForm()
    return render(request, 'police.html', {'form':form})

@login_required(login_url='/accounts/login')
def post_health(request):
    if request.method == 'POST':
        form = UpdateHealthForm(request.POST,request.FILES)
        if form.is_valid():
            center = form.save(commit=False)
            center.save()
            return redirect('home')
    
    else:
        form = UpdateHealthForm()
    return render(request, 'health.html', {'form':form})
