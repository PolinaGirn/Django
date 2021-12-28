from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def get_catalog_menu():
    return ProductCategory.objects.all()


def index(request):
    context = {
        'page_title': 'главная',
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'каталог',
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/products.html', context)


def category_items(request, category_pk):
    if category_pk == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=category_pk)

    context = {
        'page_title': 'каталог',
        'catalog_menu': get_catalog_menu(),
        'products': products,
        'category_pk': category_pk,
    }
    return render(request, 'mainapp/category_items.html', context)


def contact(request):
    _locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Краснодар',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
    ]

    context = {
        'page_title': 'контакты',
        'locations': _locations,
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/contact.html', context)
