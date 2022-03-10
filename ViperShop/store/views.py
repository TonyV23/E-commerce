from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product,Cart,Order

# Create your views here.
def index(request):
    products = Product.objects.all() # get all entries of database
    return render(request, 'store/index.html', context={'products' : products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug = slug)
    # return HttpResponse(product.name)
    # return HttpResponse(f'{product.name} {product.price} fbu')
    return render(request, 'store/detail.html', context={'product' : product})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug = slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,ordered=False, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else :
        order.quantity += 1
        order.save()
    
    return redirect(reverse( 'product', kwargs={"slug":slug}))

def cart(request):
    cart = get_object_or_404(Cart,user= request.user)

    return render(request, 'store/cart.html', context={"orders":cart.orders.all()})

def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()

    return redirect('index')