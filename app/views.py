from .models import Food,Category,Comment
from .serializer import FoodSerializer,CategorySerializer,CommentSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .my_permissions import CategoryPermission,FoodPermission,CommentPermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle

class CategoryAnonThrottle(AnonRateThrottle):
    scope = "category_list"

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = "category_id"
    lookup_field = "pk"
    throttle_classes = [CategoryAnonThrottle]

    # permission_classes = [permissions.IsAuthenticated , CategoryPermission]


class FoodAnonThrottle(AnonRateThrottle):
    scope = "foods_list"

class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_url_kwarg = "food_id"
    lookup_field = "pk"
    throttle_classes = [FoodAnonThrottle]


class CommentAnonThrottle(AnonRateThrottle):
    scope = "comments_list"

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = "comment_id"
    lookup_field = "pk"
    throttle_classes = [CommentAnonThrottle]

