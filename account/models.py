from enum import unique
import random
from tabnanny import verbose

from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.urls import reverse
from django.utils.translation import gettext_lazy
from yaml import serialize as
""" from django.shortcuts import get_object_or_404
from django.http import JsonResponse """

# Create your models here.
class Post(models.Model):
     
     status_choises - (
         ('ACTIVE', 'Active'),
         ('DRAFT', 'Draft')
     )
     title = models.CharField(max_length=255, verbose_name='Zagalovok')
     text = models.TextField
     status = models.CharField(verbose_name='Photo',
                               max_length=6, 
                               choices=status_choices, 
                               default='DRAFT')
     #photo = models.ImageField('post/imgs/', null=True)
     created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
     updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True, null=True)
     is_actual = models.BooleanField( verbose_name='is_actual', blank=True, null=True)

     user= models.ForeignKey(
                             verbose_name='User'
                             to=User, 
                             related_name='posts', 
                             on_delete=models.CASCADE
                             )
     categories = models.ManyToManyField (
         verbose_name='Categories'
         to = 'Category',
         related_name='posts',
     )

     def __str__(self) -> str:
         return f'{self.id} --- {self.title}'
     
     def get_absolute_url(self):
         return reverse("detail_post", kwargs={"pk": self.pk})
    class Meta:
         db_table = 'Post'
         ordering = ['-created_at']
         verbose_name = 'Post'
         verbose_name_plural = 'Posts'


class Category(models.Model):
    title = models.CharField(
        verbose_name = 'Categoruu',
        max_length=255,
        unique=True,
        )
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True, null=True)
    is_actual = models.BooleanField( verbose_name='is_actual', blank=True, null=True)

    def __str__(self) -> str:
         return f'{self.id} --- {self.title}'
     
    def get_absolute_url(self):
         return reverse("detail_post", kwargs={"pk": self.pk})
    
    class Meta:
        db_table = 'Post'
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    
class Post_new(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
class PostAPIUpdate (generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostAPIDestroy (generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminUser,)
class DeletePostView(View):
    model = None

class PostDeleteView(DeletePostView):
    model = Post
    
