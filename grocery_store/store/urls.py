from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.product_list, name="product_list"),
    path('add_product/', views.add_product, name="add_product"),
    path('delete_product/<int:pk>/', views.delete_product, name="delete_product"),
    path('place_order/', views.place_order, name="place_order"),
    path('order_success/', views.order_success, name='order_success'),
    path('get_product_price/<int:product_id>/', views.get_product_price, name='get_product_price'),
    path('contact/', views.contact, name="contact"),
]
