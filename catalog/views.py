from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category, Company

def index(request):
    categories = Category.objects.all()
    latest_products = Product.objects.select_related(
        'category', 'company'
    ).order_by('-id')[:6]
    return render(request, 'catalog/index.html', {
        'categories': categories,
        'latest_products': latest_products,
    })

def product_list(request):
    products = Product.objects.select_related('category', 'company')
    categories = Category.objects.all()

    # search
    q = request.GET.get('q')
    if q:
        products = products.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(company__name__icontains=q)
        )

    # category filter
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # price filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'categories': categories,
    })

def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.select_related('category', 'company'), 
        pk=pk
    )
    return render(request, 'catalog/product_detail.html', {
        'product': product,
    })