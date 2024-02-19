from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Pin, Tag, User
from .forms import PinForm, CreateUserForm

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    pins = Pin.objects.filter(
        Q(tags__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    
    context = {'pins': pins,
               }
    return render(request, 'base/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
    
    context = {'page': page}
    return render(request, 'base/login-register.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login-register.html', {'form': form})

@login_required
def createPin(request):
    form = PinForm()
    
    topics = Tag.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('Tag')
        topic, created = Tag.objects.get_or_create(name=topic_name)

        Pin.objects.create(
            pinner=request.user,
            tags=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            picture = request.POST.get('picture')
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
            
    return render(request, 'base/create-pin.html', context)