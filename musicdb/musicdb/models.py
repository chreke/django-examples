from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(
        Artist,
        related_name="albums",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=32)
    genre = models.CharField(max_length=16)
    release_date = models.DateField()
    length = models.DurationField()

    def __str__(self):
        return f"{self.title} ({self.release_date.year})"
