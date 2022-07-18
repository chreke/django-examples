from django.db import models


class User(models.Model):
	username = models.SlugField(unique=True)
	followers = models.ManyToManyField("User", related_name="following")

	def __str__(self):
		return self.username
