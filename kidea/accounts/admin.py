from django.contrib import admin

# Register your models here.

from .models import Member
from .models import Product
from .models import ShoppingCart

admin.site.register(Member)
admin.site.register(Product)
admin.site.register(ShoppingCart)


