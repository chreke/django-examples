from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer

class CreateAccountView(CreateAPIView):
    serializer_class = UserSerializer

