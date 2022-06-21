from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Album, Artist


class AlbumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ["title", "url"]


class AlbumDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ["artist", "title" "genre", "release_date", "length", "url"]


class ArtistSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ["name", "url"]


class ArtistDetailSerializer(HyperlinkedModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ["albums", "name", "url"]
