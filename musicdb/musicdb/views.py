from rest_framework.viewsets import ModelViewSet

from .models import Album, Artist
from .serializers import (
    AlbumSerializer,
    AlbumDetailSerializer,
    ArtistSerializer,
    ArtistDetailSerializer,
)


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArtistSerializer
        return ArtistDetailSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AlbumSerializer
        return AlbumDetailSerializer
