from django.contrib import admin
from .models import Product
from .models import VolumeType
from .models import Comment
from .models import Card



# Register your models here.
admin.site.register(Product)
admin.site.register(VolumeType)
admin.site.register(Comment)
admin.site.register(Card)