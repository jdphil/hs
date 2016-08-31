from django.contrib import admin
from .models import Habit, User_Habit

admin.site.register(Habit)
admin.site.register(User_Habit)