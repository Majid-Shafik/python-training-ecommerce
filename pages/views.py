from django.shortcuts import render ,get_object_or_404

from  .models import Product,Category
from decimal import Decimal

# Create your views here.

def home(request):
    products = []  # This would typically be fetched from the database
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': products ,'categories':categories})

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop.html', {'products': products, 'categories': categories})

def shop_category(request, category_id):
    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)
    if category:
        # Handle the case where the category does not exist
        products = Product.objects.filter(category=category)
    elif category_id == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.none()


    categories = Category.objects.all()
    return render(request, 'shop.html', {'products': products, 'categories': categories})

# show details of a products
def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    diff =  product.price * Decimal('0.2')
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'shop-details.html', {'product': product, 'related_products': related_products, 'diff': diff})


def shop_cart(request):
    return render(request, 'shopping-cart.html')
def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')