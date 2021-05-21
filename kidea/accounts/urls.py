from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('browse/', views.browse, name="browse"),
    path('quotation/', views.quotation, name="quotation"),
    path('singleproduct/<str:pk>/', views.singleproduct, name="singleproduct"),
    path('systemcabinetQuotation/', views.systemcabinetQuotation, name="systemcabinetQuotation"),
    path('singleproduct2/<str:slug>/<int:id>', views.singleproduct2, name="singleproduct2"),
]


