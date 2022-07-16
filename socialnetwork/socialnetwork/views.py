from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    @action(detail=True, methods=["get"])
    def followers(self, request, username):
        user = self.get_object()
        serializer = self.get_serializer(user.followers, many=True)
        return Response(serializer.data)
