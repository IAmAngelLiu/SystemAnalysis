from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
#from django.contrib.auth.views import logout_then_login
# from django.contrib.auth.views import password_change
# from django.contrib.auth.views import password_change_done
# from django.contrib.auth.views import password_reset
# from django.contrib.auth.views import password_reset_complete
# from django.contrib.auth.views import password_reset_confirm
# from django.contrib.auth.views import password_reset_done

urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('browse/', views.browse, name="browse"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('quotation/', views.quotation, name="quotation"),
    path('singleproduct/<str:pk>/', views.singleproduct, name="singleproduct"),
    path('systemcabinetQuotation/', views.systemcabinetQuotation, name="systemcabinetQuotation"),
    path('singleproduct2/<str:slug>/<int:id>', views.singleproduct2, name="singleproduct2"),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),

    #url(r'^$', views.dashboard, name='dashboard'),
    #url(r'^register/$', views.register, name='register'),

    # login logout
    #url(r'^login/$', login, name='login'),
    #url(r'^logout/$', logout, name='logout'),
    #url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

    # # change password
    # url(r'^password-change/$', password_change, name='password_change'),
    # url(r'^password-change/done/$', password_change_done, name='password_change_done'),

    # # reset password
    # # restore password urls
    # url(r'^password-reset/$',
    #     password_reset,
    #     name='password_reset'),
    # url(r'^password-reset/done/$',
    #     password_reset_done,
    #     name='password_reset_done'),
    # url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
    #     password_reset_confirm,
    #     name='password_reset_confirm'),
    # url(r'^password-reset/complete/$',
    #     password_reset_complete,
    #     name='password_reset_complete'),
]


