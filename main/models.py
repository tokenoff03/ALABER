from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукт")
    descriptioon = models.TextField(verbose_name="Описание")
    cost = models.FloatField(verbose_name="Цена")
    available_amount = models.IntegerField(verbose_name="Есть в наличии")
    volume_type = models.ForeignKey("VolumeType", on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to="products", null=True)

    def __str__(self):
        return f"{self.name} - {self.descriptioon}"


class VolumeType(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тип объема")

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    username = models.CharField(max_length=150, verbose_name="Имя пользователя")
    text = models.TextField(verbose_name="Коммент")
    img = models.ImageField(verbose_name="Картинка", null=True, blank=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name="Продукт")

    def __str__(self):
        return f"{self.username}: {self.text}"


class Card(models.Model):
    number = models.IntegerField(verbose_name="Номер карты")
    username = models.CharField(max_length=100, verbose_name="Имя на карточке")
    month = models.IntegerField(verbose_name="Месяц истечения времени", null=True)
    year = models.IntegerField(verbose_name="Год истечения времени", null=True)
    num = models.IntegerField(verbose_name="CVV2/CVC2", null=True)

    def __str__(self):
        return f"{self.number}"

