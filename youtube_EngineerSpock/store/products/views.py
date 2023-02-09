from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView

from products.models import ProductCategory, Product, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = 'Narek'
        context['is_promotion'] = False
        context['title'] = 'Shop'
        return context


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page)

    context = {
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
        'title': 'Store - Каталог'
    }

    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
