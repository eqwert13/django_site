from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from django.shortcuts import render
from .forms import PasswordForm
import random
import string


def generate_password(request):
    password = None

    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            chars = ""
            if form.cleaned_data["uppercase"]:
                chars += string.ascii_uppercase
            if form.cleaned_data["lowercase"]:
                chars += string.ascii_lowercase
            if form.cleaned_data["digits"]:
                chars += string.digits
            if form.cleaned_data["symbols"]:
                chars += string.punctuation

            if chars:
                length = int(form.cleaned_data["length"])
                password = "".join(random.choice(chars) for _ in range(length))
    else:
        form = PasswordForm()

    return render(
        request, "myapp/generate_password.html", {"form": form, "password": password}
    )


# def index(request):
#     items = Product.objects.all()
#     context = {"items": items}
#     return render(request, "myapp/index.html", context)


class ProductListView(ListView):
    model = Product
    template_name = "myapp/index.html"
    context_object_name = "items"


# def indexItem(request, my_id):
#     item = Product.objects.get(id=my_id)
#     context = {"item": item}
#     return render(request, "myapp/detail.html", context=context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "myapp/detail.html"
    context_object_name = "item"


@login_required
def add_item(reqest):
    if reqest.method == "POST":
        name = reqest.POST.get("name")
        price = reqest.POST.get("price")
        description = reqest.POST.get("description")
        image = reqest.FILES["upload"]
        seller = reqest.user
        item = Product(
            name=name, price=price, description=description, image=image, seller=seller
        )
        item.save()

    # code to add a new item
    return render(reqest, "myapp/additem.html")


@login_required
def update_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/myapp/")
    context = {"item": item}
    return render(request, "myapp/updateitem.html", context)


@login_required
def delete_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/myapp/")
    context = {"item": item}
    return render(request, "myapp/deleteitem.html", context)


def about(request):
    return render(request, "myapp/about.html")


def contacts(request):
    return render(request, "myapp/contacts.html")
