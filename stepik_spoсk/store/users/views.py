from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileFolm
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'Store - Авторизация'


class UserRegisterView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались!'
    title = 'Store - Регистрация'


class UserPrifileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileFolm
    template_name = 'users/profile.html'
    title = 'Store - Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserPrifileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context
