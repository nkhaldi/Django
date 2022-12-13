from django.db import models
from django.utils.translation import gettext_lazy


class Product(models.Model):
    class Meta:
        verbose_name = gettext_lazy('product')
        verbose_name_plural = gettext_lazy('products')
        ordering = ['title']

    title = models.CharField(gettext_lazy('title'), max_length=255)
    sku = models.CharField(gettext_lazy('sku'), max_length=255, unique=True)
    slug = models.SlugField(gettext_lazy('slug'), max_length=255)
    category = models.ForeignKey(verbose_name=gettext_lazy('category'), to='Category', on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = gettext_lazy('category')
        verbose_name_plural = gettext_lazy('categories')
        ordering = ['title']

    title = models.CharField(gettext_lazy('title'), max_length=255)
    slug = models.SlugField(gettext_lazy('slug'), max_length=255)
    property_objects = models.ManyToManyField(verbose_name=gettext_lazy('properties'), to='PropertyObject')

    def __str__(self):
        return self.title


class PropertyObject(models.Model):
    class Meta:
        verbose_name = gettext_lazy('property object')
        verbose_name_plural = gettext_lazy('properties objects')
        ordering = ['title']

    class Type(models.TextChoices):
        STRING = 'string', gettext_lazy('string')
        DECIMAL = 'decimal', gettext_lazy('decimal')

    title = models.CharField(gettext_lazy('title'), max_length=255)
    code = models.SlugField(gettext_lazy('code'), max_length=255)
    value_type = models.CharField(gettext_lazy('value type'), max_length=10, choices=Type.choices)

    def __str__(self):
        return f'{self.title} ({self.get_value_type_display()})'


class PropertyValue(models.Model):
    class Meta:
        verbose_name = gettext_lazy('property value')
        verbose_name_plural = gettext_lazy('properties values')
        ordering = ['value_string', 'value_decimal']

    property_object = models.ForeignKey(to=PropertyObject, on_delete=models.PROTECT)
    value_string = models.CharField(gettext_lazy('value string'), max_length=255, blank=True, null=True)
    value_decimal = models.DecimalField(gettext_lazy('value decimal'), max_digits=11, decimal_places=2, blank=True, null=True)
    code = models.SlugField(gettext_lazy('code'), max_length=255)
    products = models.ManyToManyField(to=Product, related_name='properties')

    def __str__(self):
        return str(getattr(self, f'value_{self.property_object.value_type}', None))
