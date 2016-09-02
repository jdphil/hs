from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
   if request.user.is_authenticated and not request.user.is_anonymous:	
       return redirect('/habits')	
   return render(request, 'index.html')


def about(request):
   return render(request, 'about.html')


def contact(request):
   return render(request, 'login.html')


@login_required
def habits(request):
	return render(request, 'habits.html', {'user' : request.user})


def successfully_logged_out(request):
	return redirect('/')


def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    username = request.POST['email']
    password = request.POST['password']
    u = User.objects.create_user(username, email, password)
    u.last_name = last_name
    u.first_name = first_name
    u.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/habits')
    else:
         return redirect('/')