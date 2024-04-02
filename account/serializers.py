from email.policy import default
from rest_framework import serializers


class PostListSerializer(serializers.Serializer):
    user = serializer.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField()
    is_active = serializers.BooleanField()

class PostCreateSerializer(serializers.Serializer):
    title =serializers.CharField()
    is_active = serializers.BooleanField()
    user = serializers.IntegerField()
    categories = serializers.ListField()

