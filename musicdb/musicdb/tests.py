from django.test import TestCase

from rest_framework.test import APIClient

from .models import Artist, Album

class AlbumViewTestCase(TestCase):
    def setUp(self):
        self.artist = Artist(name="The Wild Gooseberries")
        self.artist.save()

    def test_creating_album(self):
        APIClient().post(
            "/albums/",
            {
                "artist": self.artist.pk,
                "title": "Mental Mind",
                "genre": "Jazz",
                "release_date": "2020-10-11",
                "length": "00:55:10",
            },
            format="json"
        )
