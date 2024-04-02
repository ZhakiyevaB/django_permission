import json

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

from django.urls import reverse
from requests import Response

from .post.models import Post
from .models import UserAccount

from .models import Post
from .permissions import IsAdminOrReadOnly
from .serializers import PostListSerializer

class AccountAPIView(APIView):

    def get(self,request):
        account_mobile_phones = UserAccount.objects.all('mobile_phone')
        return Response (list(account_mobile_phones))
    
    def post(self,request):
        print(request.data)
        return Response('test')

class PostAPIUpdate (generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrRealOnly)
    
class PostAPIDestroy (generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminUser, IsAdminOrRealOnly)
