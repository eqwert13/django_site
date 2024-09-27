from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:index")
    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)

@login_required
def profile(request):
    return render(request, "users/profile.html")

def seller_profile(request, id):
    seller = User.objects.get(id=id)

    context = {
        "seller": seller,
    }

    return render(request, "users/sellerprofile.html", context)

