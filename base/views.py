from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Pin, Tag
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