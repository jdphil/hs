from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
   if request.user.is_authenticated:
       return redirect('/habits')	
   return render(request, 'index.html')


def about(request):
   return render(request, 'about.html')


def contact(request):
   return render(request, 'login.html')


@login_required
def habits(request):
	return render(request, 'habits.html', {'user' : request.user})
