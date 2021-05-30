from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django import forms
from django.contrib import messages
# Create your views here.

from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from .models import *


def home(request):
	return render(request, 'accounts/index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})


def login(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  #重新導向到首頁
        else:
            messages.error(request, "所輸入的使用者帳號或是密碼錯誤，請再輸入一次。")
    context = {
        'form': form
    }
    # if not user:
    return render(request, 'accounts/login.html', context)

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



# def shopping_cart(request):
#     return render(request, 'shopping_cart/index.html')


@login_required(login_url="/accounts/login")
def shopping_cart(request, id):
    cart = ShoppingCart.objects.get(id = id)
    return render(request, 'shopping_cart/index.html', {'shopping_cart': cart})

@login_required(login_url="/accounts/login")
def shopping_cart_detail(request, account_id):
    cart = ShoppingCart.objects.get(member=account_id)
    product = Product.objects.filter(id=cart.product)
    return render(request, 'shopping_cart/index.html', {'product': product})

@login_required(login_url="/accounts/login")
def shopping_cart_remove(request, product_id):
    aProduct = get_object_or_404(ShoppingCart, product=product_id)
    aProduct.delete()
    return redirect("shopping_cart")


