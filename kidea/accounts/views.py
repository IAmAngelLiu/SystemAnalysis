from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django import forms
from django.contrib import messages
# Create your views here.

from django.http import HttpResponse
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
	board_info = Board.objects.all()

	return render(request, 'accounts/systemcabinetQuotation.html', { 'boards': board_info })

def getSCQuote(request):
	board_info = Board.objects.all()

	width = request.GET.get('width')
	depth = request.GET.get('depth')
	height = request.GET.get('height')
	partition_cnt = request.GET.get('partition_cnt')
	id_back = request.GET.get('board_back')
	id_door = request.GET.get('board_door')
	id_others = request.GET.get('board_others')

	prev_data = {
		'width': width,
		'depth': depth,
		'height': height,
		'partition_cnt': partition_cnt,
		'id_back': int(id_back),
		'id_door': int(id_door),
		'id_others': int(id_others)
	}

	if(width == "" or depth == "" or height == "" or partition_cnt == ""):
		return render(request, 'accounts/systemcabinetQuotation.html', { 'boards': board_info, 'prev_data': prev_data, 'error': True })

	width = float(width)
	depth = float(depth)
	height = float(height)
	partition_cnt = float(partition_cnt)
	cnt = 0
	for board in board_info:
		if board.id == int(id_back):
			price_back = board.price
			cnt += 1
		elif board.id == int(id_door):
			price_door = board.price
			cnt += 1
		elif board.id == int(id_others):
			price_others = board.price
			cnt += 1
		if cnt == 3:
			break

	door_part = 0
	back_part = 0
	others_part = 0

	door_part += width * height / 900
	back_part += width * height / 900
	others_part += depth * height / 450
	others_part += width * depth / 450
	others_part += width * depth * (partition_cnt + 1) / 900
	others_part += 2 * width / 225
	others_part += (width + depth) / 45

	total_price = door_part * price_door + back_part * price_back + others_part * price_others

	return render(request, 'accounts/systemcabinetQuotation.html', { 'boards': board_info, 'quote_price': round(total_price), 'prev_data': prev_data, 'error': False })