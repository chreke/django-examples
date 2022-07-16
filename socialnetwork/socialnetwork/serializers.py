# socialnetwork/serializers.py

from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "followers", "following"]


