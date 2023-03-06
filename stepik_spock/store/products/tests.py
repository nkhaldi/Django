from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Narek\'s')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'goods.json']

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')

        products = Product.objects.all()
        self.assertEqual(response.context_data['object_list'], products)
