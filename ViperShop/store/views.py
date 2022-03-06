from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from store.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all() # get all entries of database
    return render(request, 'store/index.html', context={'products' : products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug = slug)
    # return HttpResponse(product.name)
    # return HttpResponse(f'{product.name} {product.price} fbu')
    return render(request, 'store/detail.html', context={'product' : product})