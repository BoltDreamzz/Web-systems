from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegisterForm, UserLoginForm


def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            # user = form.save(commit=False)
            # user.bio = request.user.bio
            # user.city = request.user.city
            # user.country = request.user.country
            form.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f"Username @{username} was created successfully!")
            return redirect("authusers:login")

    context = {"form": form}
    return render(request, "authusers/register.html", context)


def login_view(request):
    form = UserLoginForm()

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                name = form.cleaned_data.get(username)
                login(request, user)
                messages.success(request, f"Welcome !")

                return redirect("core:home")  # Redirect to dashboard later

    context = {"form": form}
    return render(request, "authusers/login.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, f"Signed out")
    return redirect("core:home")


def splash(request):
    return render(request, "authusers/splash.html")






