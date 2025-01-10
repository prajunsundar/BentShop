from django.urls import path
from .views import cart_detail,Add_cart,cart_remove,full_remove
app_name='cartapp'

urlpatterns=[
    path('cart/',cart_detail,name='cart-detail'),
    path('add/<int:product_id>/',Add_cart,name='add-cart'),
    path('remove/<int:Product_id>/',cart_remove,name='remove-cart'),
    path('full-remove/<int:Product_id>/',full_remove,name='full-remove')

]