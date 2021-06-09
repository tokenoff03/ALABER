from django import template
from main.models import Product
from django.urls import reverse
from django.shortcuts import redirect

register = template.Library()


@register.simple_tag(name="my_tag")
def resolve_product(id):
    product = Product.objects.get(pk=id)
    return f"{product.name}"


@register.simple_tag(name="my_tag_img")
def img_product(id):
    product = Product.objects.get(pk=id)
    return product.img


@register.simple_tag(name="my_tag_cost")
def cost_product(id):
    product = Product.objects.get(pk=id)
    return f"{product.cost}"




