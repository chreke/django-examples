# socialnetwork/serializers.py

from .models import User
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
)


class UserSerializer(ModelSerializer):
    followers = HyperlinkedIdentityField(
        view_name="user-followers",
        lookup_field="username",
    )

    class Meta:
        model = User
        fields = ["username", "followers", "following"]


