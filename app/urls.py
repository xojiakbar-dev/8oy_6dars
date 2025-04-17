from django.urls import path
from .views import (CategoryViewSet, FoodViewSet, CommentsViewSet)
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




urlpatterns = [
    path('category/' , CategoryViewSet.as_view({'get':'list'}) , name='category_view'),
    path('category/<int:category_id>/' , CategoryViewSet.as_view({'get': 'list' , 'put' : 'update' , 'patch' : 'partial_update' , 'delete' : 'destroy'}) , name='category_detail'),
    path('foods/' , FoodViewSet.as_view({'get':'list'}) , name='foods'),
    path('foods/<int:food_id>/' , FoodViewSet.as_view({'get': 'list' , 'put' : 'update' , 'patch' : 'partial_update' , 'delete' : 'destroy'}) , name='food_detail'),
    path('comments/' , CommentsViewSet.as_view({'get':'list'}) , name='comments'),
    path('comments/<int:comment_id>/' , CommentsViewSet.as_view({'get': 'list' , 'put' : 'update' , 'patch' : 'partial_update' , 'delete' : 'destroy'}) , name='comment_detail'),
]


