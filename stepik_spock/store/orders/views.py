from django.views.generic.base import TemplateView
# from django.views.generic.edit import CreateView


# class OrderCreateView(CreateView):
class OrderCreateView(TemplateView):
    template_name = 'orders/order-create.html'
