from django.urls import path
from .views import (CategoryView , CategoryDetailView , FoodApiView , FoodDetailView , CommentsView , CommentDetailView)
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API hujjati",
      default_version='v1',
      description="FASTFOOD API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('category/' , CategoryView.as_view() , name='category_view'),
    path('category/<int:pk>/' , CategoryDetailView.as_view() , name='category_detail'),
    path('foods/' , FoodApiView.as_view() , name='foods'),
    path('foods/<int:pk>/' , FoodDetailView.as_view() , name='food_detail'),
    path('comments/' , CommentsView.as_view() , name='comments'),
    path('comments/<int:pk>/' , CommentDetailView.as_view() , name='comment_detail'),
    path('api-token-auth/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


