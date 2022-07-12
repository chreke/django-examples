from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)

from .models import Album, Artist


class AlbumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ["title", "release_date", "url"]


class ArtistSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = ["name", "url"]


class AlbumDetailSerializer(ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = [
            "id",
            "artist",
            "artist_info",
            "title",
            "genre",
            "release_date",
            "length",
        ]


class ArtistDetailSerializer(ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["id", "albums", "name"]
