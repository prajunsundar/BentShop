from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from shopapp.models import product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
from userapp.models import Profile

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def Add_cart(request,product_id):

    products=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()


    try:
        cart_item=CartItem.objects.get(product=products,cart=cart)
        if cart_item.quantity < cart_item.product.stock :
            cart_item.quantity +=1
        cart_item.save()


    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(product=products,quantity=1,cart=cart)
        cart_item.save()

    # if request.user.is_authenticated:
    #     current_user = Profile.objects.filter(user__id=request.user.id)
    #     carty = str(cart)
    #     carty = carty.replace("\'")
    #     current_user.update(old_cart=str(carty))


    return redirect('cartapp:cart-detail')


def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))



def cart_remove(request,Product_id):
    carts=Cart.objects.get(cart_id=_cart_id(request))
    products=get_object_or_404(product,id=Product_id)
    cart_item=CartItem.objects.get(product=products,cart=carts)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart-detail')

def full_remove(request,Product_id):
    carts = Cart.objects.get(cart_id=_cart_id(request))
    products = get_object_or_404(product, id=Product_id)
    cart_item = CartItem.objects.get(product=products, cart=carts)
    cart_item.delete()
    return redirect('cartapp:cart-detail')