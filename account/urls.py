from django.contrib import admin
from django.urls import path, re_path

from account.models import PostAPIDestroy

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='list_post'),
    path('create/', views.CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail_post')
    path('about/', views.AboutView.as_view(), name='about'),
    path('api/v1/postdelete/int:pk>/', views.PostAPIDestroy.as_view(), name='destroe'),
    

]
