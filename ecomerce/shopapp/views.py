from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    men=product.objects.filter(gender='M')
    men_1=men[0]
    men_2 = men[1]
    men_3 = men[1]
    men_4 = men[1]

    women = product.objects.filter(gender='W')
    women_1 = women[0]
    women_2 = women[1]
    women_3 = women[2]
    women_4 = women[4]

    kid = product.objects.filter(gender='K')
    kid_1 = kid[0]
    kid_2 = kid[1]
    kid_3 = kid[2]
    kid_4 = kid[3]

    return render(request,'index.html',{'men1':men_1,'men2':men_2,'men3':men_3,'men4':men_4,'women1':women_1,'women2':women_2,'women3':women_3,'women4':women_4,'kid1':kid_1,'kid2':kid_2,'kid3':kid_3,'kid4':kid_4})


def men_products(request):
    men= product.objects.filter(gender='M')
    paginator = Paginator(men, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(p.num_pages)
    return render(request,'menproducts.html',{'men':page_obj})
def women_products(request):
    women= product.objects.filter(gender='W')
    paginator = Paginator(women, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(p.num_pages)
    return render(request,'womenproducts.html',{'women':page_obj})

def kid_products(request):
    kid= product.objects.filter(gender='K')
    paginator = Paginator(kid, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(p.num_pages)
    return render(request,'kidproducts.html',{'kid':page_obj})



def single_product(request,product_slug):
    try:
        products=product.objects.get(slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'single-product.html',{'product':products})








