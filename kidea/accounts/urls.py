from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('browse/', views.browse, name='browse'),
    path('quotation/', views.quotation),
    path('singleproduct/<str:name>', views.singleproduct, name='singleproduct'),
    path('systemcabinetQuotation/', views.systemcabinetQuotation),
]


