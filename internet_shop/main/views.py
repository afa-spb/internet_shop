from django.shortcuts import render
from django.http import HttpResponse
from main.models import Category, Product
from django.db.models import Count, F
from django.core.paginator import Paginator
from cart.cart import Cart
from cart.forms import CartAddProductForm
from django.urls import reverse_lazy

def main_page(request):
    products = Product.objects.order_by('-views')[:4]
    context = {'products': products}
    return render(request, 'main/main_page.html', context)


def categories(request):
    all_categories = Category.objects.annotate(x=Count('product')).filter(x__gt=0)
    context = {'all_categories': all_categories}
    return render(request, 'main/categories.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    all_products = Product.objects.filter(category=category, is_published=True)
    form_cart = CartAddProductForm()

    # счетчик посещений этой категории
    if request.GET.get('page') == None:
        category.views = F('views') + 1
    category.save()

    # пагинация
    paginator = Paginator(all_products, 40)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    # добавление товаров в корзину
    if request.method == "POST":
        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=form.cleaned_data['id_product'])
            cart.add(product=product, quantity=form.cleaned_data['quantity'])

    context = {'category': category, 'page_obj': page_obj, 'form_cart': form_cart}
    return render(request, 'main/category.html', context)


def product_card(request, pk):
    product = Product.objects.get(pk=pk)
    additional_pictures = product.imagegallery_set.all()
    form_cart = CartAddProductForm()
    product.views = F('views') + 1
    product.save()
    context = {'product': product, 'additional_pictures': additional_pictures, 'form_cart': form_cart}

    if request.method == "POST":
        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cart.add(product=product, quantity=form.cleaned_data['quantity'])

    return render(request, 'main/product_card.html', context)




