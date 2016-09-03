from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from habitstation.models import User_Habit, User_Habit_Activity
import pdb
import sys
# Create your views here.

def home(request):
   #pdb.set_trace()
   if request.user.is_authenticated() and not request.user.is_anonymous():
       print ("logged in")	
       return redirect('/habits')
   else:
       print ("NOT logged in")		
       return render(request, 'index.html')


def about(request):
   return render(request, 'about.html')


def contact(request):
   return render(request, 'login.html')


@login_required
def habits(request):
   #pdb.set_trace()
   list_habits = User_Habit.objects.filter(habit_user=request.user.id)
   return render(request, 'habits.html', {'user' : request.user, 'habs' : list_habits})


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
    current_user = authenticate(username=username, password=password)
    if current_user is not None:
        login(request, current_user)
        # Redirect to a success page.
        return redirect('/habits')
    else:
         return redirect('/')


def add_habit(request):
    #do some stuff
    try:
        current_user = request.user
        name = request.POST['habit_name']
        desc = request.POST['habit_desc']
        freq = int(request.POST['habit_freq'])
        h = User_Habit.objects.create_habit(current_user,name,desc,freq)
        print(h)
        return redirect('/habits')
    except:
        pdb.set_trace()
        print (sys.exc_info()[0])
        return redirect('/habits')