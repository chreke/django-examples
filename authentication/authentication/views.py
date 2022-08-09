from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import UserSerializer

class CreateAccountView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
