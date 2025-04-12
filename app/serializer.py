from rest_framework import serializers
from .models import Category,Food,Comment
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id' , 'name' , 'category' , 'price' , 'discount']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

