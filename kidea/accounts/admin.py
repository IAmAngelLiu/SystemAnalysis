from django.contrib import admin

# Register your models here.

from .models import Member, Product, Board, ShoppingCart

class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'address', 'cellphone', 'email', 'is_superuser', 'date_created')
    list_filter = ('is_superuser', )
    
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'amount', 'customization')
    list_filter = ('is_customized', )

admin.site.register(Member, MemberAdmin)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Board)


