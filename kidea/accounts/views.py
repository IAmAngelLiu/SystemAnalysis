from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import *

def home(request):
	return render(request, 'accounts/index.html')

def login(request):
	return render(request, 'accounts/login.html')

def register(request):
	return render(request, 'accounts/register.html')

def browse(request):
	products = Product.objects.all()
	return render(request, 'accounts/browse.html', {'products':products})

def quotation(request):
	return render(request, 'accounts/quotation.html')

def singleproduct(request, name):
	product_name = name

	product = Product.objects.get(name=product_name)
	return render(request, 'accounts/singleproduct.html', {'product':product})

def systemcabinetQuotation(request):
	return render(request, 'accounts/systemcabinetQuotation.html')




