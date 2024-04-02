from dataclasses import field
from post.models import Post
from rest_framework import serializers


class PostListSerializer(serializers.Serializer):
    title = serializers.CharField()
    is_active = serializers.BooleanField()

class PostCreateSerializer(serializers.Serializer):
    title =serializers.CharField()
    is_active = serializers.BooleanField()
    user = serializers.IntegerField()
    categories = serializers.ListField()

    
class PostListModelSerializer(serializers.Serializer):
    class Meta:
        model =Post
        field = ('title', 'status')

class PostListModelsSerializer(serializers.Serializer):

    user = serializers.IntegerField(source='id')
    class Meta:
        model =Post
        field = ('title', 'status', 'user', 'categories')