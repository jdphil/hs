from django.db import models
from django.utils import timezone

class User_Habit(models.Model):
    user = models.ForeignKey('auth.User')
    habit = models.CharField(max_length=200)
    habit_desc = models.TextField(default = '')
    habit_freq = models.IntegerField(default = 7)
    habit_streak = models.IntegerField(default = 0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
	    return '%s %s' % (self.user, self.habit)

class User_Habit_Activity(models.Model):
    habit = models.ForeignKey(User_Habit, on_delete=models.CASCADE)
    activity_desc = models.TextField(default = '')
    activity_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.habit, self.activity_date)		