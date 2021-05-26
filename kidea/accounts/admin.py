from django.contrib import admin
# from .models import Member

# Register your models here.

from .models import Member
from .models import Product

class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'address', 'cellphone', 'email', 'is_superuser', 'date_created')
    list_filter = ('is_superuser', )

admin.site.register(Member, MemberAdmin)
admin.site.register(Product)


