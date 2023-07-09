from ecommerce_application.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages

class UserRegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Replace 'home' with the desired URL after successful registration
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})

class UserLoginView(View):
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
    def get(self, request):
        logout(request)
        # Replace 'home' with the desired URL after successful logout
        return redirect('home')


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
