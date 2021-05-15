from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('browse/', views.browse),
    path('quotation/', views.quotation),
    path('singleproduct/', views.singleproduct),
    path('systemcabinetQuotation/', views.systemcabinetQuotation),
]


