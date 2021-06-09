from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "main"


urlpatterns = [
    path("index", views.index, name="Index_page"),
    path("authorization", views.authorization, name="log"),
    path("register", views.register, name="reg"),
    path("products/<int:id>", views.products, name="prod"),
    path("card/<int:id>", views.card, name="card"),
    path("cardsuc/<int:id>", views.cardsuc, name="cardsuc"),
    path("logout", views.logout_views, name="logout"),
    path("profile", views.prof, name="profile"),
    path("pay_cart<int:id>", views.pay_cart, name="pay_cart"),
    path("pay_cart_overall", views.pay_cart_overall, name="pay_cart_overall"),
    path("change_comment/<int:id>", views.change_comment, name="change_comment"),
    path("korzina", views.korzina, name="korzina"),
    path("add_cart/<int:id>", views.add_cart, name="add_cart"),
    path("delete_cart", views.delete_cart, name="delete_cart"),
    path("delete_comment/<int:id>", views.delete_comment, name="delete_comment"),
    path("change_password", views.change_password, name="change_password")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)