from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.urls import reverse 

class CustomUserManager(BaseUserManager):
	def _create_user(self,email, username, password, is_staff, is_superuser):
		email = self.normalize_email(email)
		user = self.model(email=email, username=username, is_staff=is_staff, is_superuser=is_superuser)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, username, password=None):
		return self._create_user(email, username, password, False, False)

	def create_superuser(self, email, username, password, name, address, cellphone, password2):
		email = self.normalize_email(email)
		user = self.model(email=email, username=username, name=name, address=address, cellphone=cellphone, password2=password2, is_staff=True, is_superuser=True)
		user.set_password(password)
		user.save(using=self._db)
		return user


# Create your models here.
class Member(AbstractUser):
	username = models.CharField(max_length=200, unique=True, help_text = '請輸入英文，也可以加上數字與符號。')
	name = models.CharField(max_length=100, null=True)
	address = models.CharField(max_length=200, null=True)
	cellphone = models.CharField(max_length=20, null=True)
	email = models.EmailField(max_length=254, null=True)
	password = models.CharField(max_length=20, null=True)
	password2 = models.CharField(max_length=20, null=True)
	is_superuser = models.BooleanField(default=False, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	shoppingCart = models.ManyToManyField('Product', through='ShoppingCart', blank=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
	objects = CustomUserManager()
	REQUIRED_FIELDS = ['name', 'address', 'cellphone', 'email', 'password', 'password2']

	def __str__(self):
		return self.username

	def get_user_url(self):
		return reverse("shopping_cart", args=[str(self.id)])


class Product(models.Model):
	TAG = (
		('衛浴', '衛浴'),
		('廚房', '廚房'),
		('系統櫃', '系統櫃'),
		('其他', '其他'),
		)
		

	name = models.CharField(max_length=200, null=True)
	price = models.CharField(max_length=200, null= True)
	description = models.CharField(max_length=500, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	tag = models.CharField(max_length=200, null=True, choices=TAG)
	slug = models.SlugField(null=True)

	def get_absolute_url(self):
		return reverse("singleproduct", args=[str(self.id)])
	

class Board(models.Model):
	TYPE = (
		('back', 'back'),
		('door', 'door'),
		('others', 'others'),
	)

	name = models.CharField(max_length=200, null=True)
	board_type = models.CharField(max_length=200, null=True, choices=TYPE)
	price = models.FloatField(null=True)

	def _str_(self):
		return self.name

class ShoppingCart(models.Model):
	member = models.ForeignKey('Member', on_delete=models.CASCADE)
	product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True)
	amount = models.IntegerField()
	price = models.FloatField(null=True)
	is_customized = models.BooleanField(default=False, null=True)
	customization = models.CharField(max_length=200, null=True, blank=True, help_text = '寬, 深, 高, 隔板數量, 背板板材, 門板板材, 櫃體板材')

	# def __str__(self):
	# 	return '{0}, {1}'.format(self.member, self.product)








