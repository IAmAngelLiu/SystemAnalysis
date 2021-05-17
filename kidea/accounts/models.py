from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(primary_key=True, max_length=200)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=254)
	address = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)
	# products in shopping cart
	product = models.ManyToManyField(Product, through='ShoppingCart')

	def _str_(self):
		return self.name


class Product(models.Model):
	TAG = (
		('衛浴', '衛浴'),
		('廚房', '廚房'),
		('系統櫃', '系統櫃'),
		('其他', '其他'),
		)
		

	name = models.CharField(primary_key=True, max_length=200)
	price = models.FloatField(null= True)
	description = models.CharField(max_length=500, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	tag = models.CharField(max_length=200, null=True, choices=TAG)


class ShoppingCart(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	amount = models.IntegerField()












