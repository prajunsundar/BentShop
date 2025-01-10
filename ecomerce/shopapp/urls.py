from django.urls import path
from .views import index,men_products,single_product,women_products,kid_products
app_name='shopapp'


urlpatterns = [
    path('',index,name='index'),
    path('men_product/',men_products,name='men_products'),
    path('women_product/',women_products,name='women_products'),
    path('kid_product/',kid_products,name='kid_products'),
    path('product:/<slug:product_slug>/',single_product,name='single-product'),



    
]
