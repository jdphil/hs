from django.db import models
from django.utils import timezone


class Habit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name

class User_Habit(models.Model):
	user = models.ForeignKey('auth.User')
	habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
	created_date = models.DateTimeField(
            default=timezone.now)

	def __str__(self):
		return '%s %s' % (self.habit, self.user)

		