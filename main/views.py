from django.shortcuts import render
from .models import Product
from .models import Comment
from .forms import CommentForm
from .forms import CardForm
from .models import Card
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from cloudipsp import Api, Checkout
from functools import reduce


api = Api(merchant_id=1396424, secret_key="test")
checkout = Checkout(api)

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "main/Index.html", {"products": products})


def authorization(request):
    if request.user.is_authenticated:
        return render(request, "main/index.html", {})
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["pass"]
            user = authenticate(username=username, password=password)

            if user != None:
                login(request, user)
                return redirect(reverse('main:Index_page'))
            else:
                return redirect(reverse('main:log'))
        return render(request, "main/authorization.html", {})


def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            email = request.POST["email"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            return redirect(reverse('main:log'))
        return render(request, "main/register.html", {})
    else:
        return render(request, "main/index.html", )



def prof(request):
    if request.user.is_authenticated:
        return render(request, "main/profile.html", {})
    else:
        return redirect(reverse("main:log"))


def products(request, id):
    product = Product.objects.get(pk=id)
    comments = Comment.objects.filter(product__pk=id)
    if request.method == "POST" and request.user.is_authenticated:
        username = request.user.username
        d = {"username": username,
             "text": request.POST["text"],
             "product": product
             }
        comment_form = CommentForm(d, request.FILES)
        if comment_form.is_valid():
            comment_form.save()
            return redirect(reverse('main:prod', args=(id,)))

    return render(request, "main/products.html", {"p": product, "comments": comments})


def card(request, id):
    prodcard = Product.objects.get(pk=id)
    if request.method == "POST":
        d = {
            "number": request.POST["number"],
            "username": request.POST["username"],
            "month": request.POST["month"],
            "year": request.POST["year"],
            "num": request.POST["num"]
        }

        card_form = CardForm(d, request.FILES)

        if card_form.is_valid():
            card_form.save()
            return redirect(reverse('main:cardsuc', args=(id,)))

    return render(request, "main/card.html", {"l": prodcard})


def cardsuc(request, id):
    cardsuc = Product.objects.get(pk=id)
    return render(request, "main/cardsuc.html", {"s": cardsuc})


def logout_views(request):
    logout(request)
    return redirect(reverse("main:Index_page"), {})


def pay_cart(request, id):
    product = Product.objects.get(pk=id)
    if request.user.is_authenticated:
        data = {"currency": "KZT", "amount": int(product.cost * 100)}
        url = checkout.url(data).get("checkout_url")
        return redirect(url)
    else:
        return redirect(reverse("main:log"))


def change_comment(request, id):
    comment = Comment.objects.get(pk=id)
    if request.user.is_authenticated:
        if request.method == "POST":
            text = request.POST["text"]
            comment.text = text
            comment.save()
            return redirect(reverse('main:Index_page', ))
        return render(request, "main/change_comment.html", {"g": comment})
    else:
        return redirect(reverse("main:log"))


def korzina(request):
    if request.user.is_authenticated:
        return render(request, "main/korzina.html", {})
    else:
        return redirect(reverse("main:log"))


def add_cart(request, id):
    cart = request.session.get("cart", [])
    cart.append(id)
    request.session["cart"] = cart
    return redirect(reverse("main:prod", args=(id,)))


def pay_cart_overall(request):
    if request.user.is_authenticated:
        cart = [Product.objects.get(pk=id) for id in request.session["cart"]]
        cost = reduce(lambda x, y: x + y, [c.cost for c in cart])
        data = {"currency": "KZT", "amount": int(cost * 100)}
        url = checkout.url(data).get("checkout_url")
        return redirect(url)
    else:
        return redirect(reverse("main:log"))


def delete_cart(request):
    request.session["cart"] = []
    return redirect(reverse("main:korzina"))


def delete_comment(request, id):
    if request.user.is_authenticated:
        Comment.objects.get(pk=id).delete()
        return redirect(reverse("main:Index_page"))


def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            password = request.POST["password"]
            user = request.user
            user.set_password(
                password
            )
            user.save()
            return redirect(reverse("main:profile"))
        return render(request, "main/change_password.html",)
    else:
        return redirect(reverse("main:log"))


