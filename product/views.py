from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Product,Category
from django.db.models import Q
def index(request):
    product_list = Product.objects.get_queryset().order_by('id')
    categories =Category.objects.all()
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
        'categories' : categories
    }
    return render(request, 'product/index.html',context)
    
def getAll(request): pass
def GetById(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    context = {
        'product': product
    }
    return render(request, 'product/detail.html', context)

def GetByCategoryId(request,category_id):
    
    products =Product.objects.filter(category_id=category_id)
    context = {
        'products': products,
        
    }
    return render(request, 'product/category.html', context)
def GetAll(request): pass
