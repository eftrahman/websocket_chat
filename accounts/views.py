from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accounts:profile")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form":form})


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


