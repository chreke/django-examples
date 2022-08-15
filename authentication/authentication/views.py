from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response

from .serializers import UserSerializer

class CreateUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class MeView(APIView):
    def get(self, request, format=None):
        return Response(UserSerializer(request.user).data)
