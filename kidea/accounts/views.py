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