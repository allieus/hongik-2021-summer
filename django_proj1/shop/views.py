from django.shortcuts import render

from shop.models import Item


def index(request):
    qs = Item.objects.all()  # QuerySet
    return render(request, "shop/item_list.html", {
        "item_list": qs,
    })


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, "shop/item_detail.html", {
        "item": item,
    })
