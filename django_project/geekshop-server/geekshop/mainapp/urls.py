from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.products, name='products'),
    path('category/<int:category_pk>/', mainapp.category_items, name='category_items'),
    path('contact/', mainapp.contact, name='contact'),
]
