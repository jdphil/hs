from django.db import models
from django.utils import timezone

class HabitManager(models.Manager):
    def create_habit(self, habit_user, habit, habit_desc, habit_freq):
        habit = self.create(habit_user=habit_user,habit=habit, habit_desc=habit_desc, habit_freq=habit_freq)
        #what should i do with the book?
        return habit

class User_Habit(models.Model):
    habit_user = models.ForeignKey('auth.User')
    habit = models.CharField(max_length=200)
    habit_desc = models.TextField(default = '')
    habit_freq = models.IntegerField(default = 7)
    habit_streak = models.IntegerField(default = 0)
    created_date = models.DateTimeField(default=timezone.now)

    objects = HabitManager()

    def __str__(self):
	    return '%s %s' % (self.habit_user, self.habit)

class User_Habit_Activity(models.Model):
    habit = models.ForeignKey(User_Habit, on_delete=models.CASCADE)
    activity_desc = models.TextField(default = '')
    activity_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.habit, self.activity_date)		