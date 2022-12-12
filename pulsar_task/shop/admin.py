from django.contrib import admin

from shop.models import Product, Category, PropertyObject, PropertyValue


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(PropertyObject)
class PropertyObjectModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'code': ['title']
    }


@admin.register(PropertyValue)
class PropertyValueModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'code': ['value_string', 'value_decimal']
    }
