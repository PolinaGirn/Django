from django.http import HttpResponseRedirect

from basketapp.models import Basket


def index(request):
    pass


def add(request, pk):
    # basket_item = request.user.basket_set.filter(
    basket_item = request.user.basket.filter(
        product_id=pk
    ).first()
    # basket_item = Basket.objects.filter(
    #     user=request.user,
    #     product_id=pk
    # ).first()
    if not basket_item:
        basket_item = Basket.objects.create(
            user=request.user,
            product_id=pk
        )

    basket_item.quantity += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
