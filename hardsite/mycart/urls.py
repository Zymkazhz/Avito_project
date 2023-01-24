from django.urls import path
from . import views as cart_views

app_name = 'cart'

urlpatterns = [
    path('', cart_views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/<category>/',
         cart_views.cart_add,
         name='cart_add'),
    path('remove/<int:product_id>/<category>/',
         cart_views.cart_remove,
         name='cart_remove'),
]