from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView, ProductAPIView, ProductDetailAPIView, CustomAuthToken, RegisterAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('auth/login/', CustomAuthToken.as_view(), name='api_login'),
    path('auth/register/', RegisterAPIView.as_view(), name='api_register'),
]
