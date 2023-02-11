from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from products.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileFolm
from users.models import User


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    # messages.success(request, 'Вы успешно зарегистрировались!')

    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserPrifileView(UpdateView):
    model = User
    form_class = UserProfileFolm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserPrifileView, self).get_context_data()
        context['title'] = 'Store - Профиль'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context
