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

def singleproduct(request, pk):
	products = Product.objects.all()
	pro = Product.objects.get(id=pk)
	context = {'pro': pro, 'products': products}
	return render(request, 'accounts/singleproduct.html', context)

def singleproduct2(request, slug, id):
	product = Product.objects.get(id=id)
	# product = Product.objects.get_absolute_url(id=id)
	return render(request, 'accounts/singleproduct2.html', {'product': product})


def systemcabinetQuotation(request):
	return render(request, 'accounts/systemcabinetQuotation.html')




