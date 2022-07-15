from django.db import models


class User(models.Model):
	username = models.CharField(max_length=32, unique=True)
	followers = models.ManyToManyField("User", related_name="following")

	def __str__(self):
		return self.username
