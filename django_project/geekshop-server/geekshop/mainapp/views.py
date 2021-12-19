import json
import os

from django.shortcuts import render

# Create your views here.
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'}
]

module_dir = os.path.dirname(__file__)

links_catalog = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contacts', 'name': 'контакты'},
]


def index(request):
    content = {
        'title': 'Главная',
        'links_catalog': links_catalog,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))

    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'links_catalog': links_catalog,
        'products': products
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {
        'title': 'Главная',
        'links_catalog': links_catalog,
    }
    return render(request, 'mainapp/contact.html', content)


def context(request):
    content = {
        'title': 'магазин',
        'header': 'Добро пожаловать на сайт',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Стулья', 'price': '4535'},
            {'name': 'Диваны', 'price': '1535'},
            {'name': 'Кровати', 'price': '2535'},
        ]
    }

    return render(request, 'mainapp/test_context.html', content)


def main(request):
    title = 'главная'

    products = Product.objects.all()[:3]

    content = {
        'title': title,
        'products': products

    }

    return render(request, 'mainapp/index.html', content)




