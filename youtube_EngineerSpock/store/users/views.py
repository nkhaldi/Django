from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from products.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileFolm
from users.models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm

    context = {
        'form': form,
        'title': 'Store - Авторизация'
    }
    return render(request, 'users/login.html', context)


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


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
