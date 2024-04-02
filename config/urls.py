
from django.urls import path, re_path

from . import views
urlpatterns = [
    path('', views.AccountAPIView.as_view(), name='account'),

]
