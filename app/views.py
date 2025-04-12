from .models import Food,Category,Comment
from .serializer import FoodSerializer,CategorySerializer,CommentSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .my_permissions import CategoryPermission,FoodPermission,CommentPermission

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [permissions.IsAuthenticated , CategoryPermission]

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [permissions.IsAuthenticated]

class FoodApiView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    permission_classes = [permissions.IsAuthenticated , FoodPermission]


class CommentsView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticated , CommentPermission]
