from django.views.generic import TemplateView
from django.http import JsonResponse
from ecommerce_application.forms import CustomUserCreationForm, CategoryForm, ProductForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from ecommerce_application.models import Category, Product
from django.contrib.auth.models import User

class UserRegisterView(View):
    """
        Class for user registration process.
    """

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        """
            Class for user registration.
        """
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Replace 'home' with the desired URL after successful registration
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})


class UserLoginView(View):
    """
        Class for user login.
    """

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have been successfully logged in.')
            # Replace 'home' with the desired URL after successful login
            return redirect('home')
        return render(request, 'registration/login.html', {'form': form})


class UserLogoutView(View):
    """
        class user logout.
    """

    def get(self, request):
        logout(request)
        # Replace 'home' with the desired URL after successful logout
        return redirect('home')

class HomeView(View):
    """
    Class for dashboard/home view.
    """

    def get(self, request):
        total_products = Product.objects.count()
        total_categories = Category.objects.all()
        total_user = User.objects.count()

        context = {
            'total_products': total_products,
            'total_categories_count': total_categories.count(),
            'total_user': total_user,
            'total_categories': total_categories
        }

        return render(request, 'home.html', context)
    
class ProductsByCategoryView(View):
    """
    Class for displaying products under a specific category.
    """

    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(categories=category)
        total_categories = Category.objects.all()
        context = {
            'category': category,
            'products': products,
            'total_categories': total_categories,
        }

        return render(request, 'product/products_by_category.html', context)




class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product/product_list.html', {'products': products})


class ProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product/product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'product/product_form.html', {'form': form})


class ProductEditView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product/product_form.html', {'form': form})

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'product/product_form.html', {'form': form})


class ProductDeleteView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product/product_confirm_delete.html', {'product': product})

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('product_list')


class CategorytListView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'category/category_list.html', {'category': category})


class CategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'category/category_form.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Category_list')
        return render(request, 'category/category_form.html', {'form': form})


class CategoryEditView(View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 'category/category_form.html', {'form': form})

    def post(self, request, pk):
        product = Category.objects.get(pk=pk)
        form = CategoryForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Category_list')
        return render(request, 'category/category_form.html', {'form': form})


class CategoryDeleteView(View):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        return render(request, 'category/category_confirm_delete.html', {'category': category})

    def post(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return redirect('Category_list')

