from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"


class FollowersListView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs["username"])
        return user.followers
