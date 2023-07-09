from django.urls import path
from ecommerce_application.views import UserRegisterView, UserLoginView, UserLogoutView, HomeView, ProductListView, ProductView, ProductEditView, ProductDeleteView, CategoryView, CategoryEditView, CategoryDeleteView, CategorytListView, ProductsByCategoryView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductView.as_view(), name='product_create'),
    path('products/edit/<int:pk>/', ProductEditView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/',
         ProductDeleteView.as_view(), name='product_delete'),

    path('category/', CategorytListView.as_view(), name='Category_list'),
    path('category/add/', CategoryView.as_view(), name='Category_create'),
    path('category/edit/<int:pk>/',
         CategoryEditView.as_view(), name='Category_edit'),
    path('category/delete/<int:pk>/',
         CategoryDeleteView.as_view(), name='Category_delete'),
    path('products/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
    path('', HomeView.as_view(), name='home'),
]
