from django.contrib import admin

# Register your models here.

from .models import Member, Product, Board


admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Board)

