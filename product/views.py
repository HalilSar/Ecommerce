from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Product,Category
from home.models import Setting
from django.db.models import Q
def index(request):
    product_list = Product.objects.get_queryset().order_by('id')
    categories =Category.objects.all()
    settings = Setting.objects.get(pk=1)
    query = request.GET.get('q')
    if query:
        product_list = product_list.filter(
            Q(productname__icontains=query) |
            Q(description__icontains=query) 
        ).distinct()
    
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {
        'products': products,
        'categories' : categories,
        'settings': settings,
    }
    return render(request, 'product/index.html',context)
    
# def getAll(request): pass
def GetById(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    categories =Category.objects.all()
    settings= Setting.objects.get(pk=1)
    context = {
        'product': product,
        'categories' : categories,
        'settings': setting,
    }
    return render(request, 'product/detail.html', context)

def GetByCategoryId(request,category_id,slug):
    
    products =Product.objects.filter(category_id=category_id)
    categories =Category.objects.all()
    settings = Setting.objects.get(pk=1)
    # paginator = Paginator(product_list, 3)
    # page_number = request.GET.get('page')
    # products = paginator.get_page(page_number)
    context = {
        'products': products,
        'categories' : categories,
        'settings': settings,
    }
    return render(request, 'product/category.html', context)
def GetAll(request): pass
