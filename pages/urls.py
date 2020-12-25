from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home'),
	path('customer/', views.customer, name='customer'),
	path('products/', views.products, name='products'),
	path('product_details/', views.product_details, name='product_details'),
	path('checkout/', views.checkout, name='checkout'),
	path('finance/', views.finance, name='finance'),


]
