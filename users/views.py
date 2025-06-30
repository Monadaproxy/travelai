from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from trips.models import Trip


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = '/users/login/'

    def get_user_context(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items() + list(c_def.items())))


@login_required
def profile_edit(request, username):
    try:
        profile = request.user.profile
    except Exception:
        Profile.objects.create(user=request.user)
        profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=username)
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'users/profile_edit.html', {'form' : form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    try:
        profile = request.user.profile
    except Exception:
        Profile.objects.create(user=request.user)
        profile = request.user.profile

    context = {
        'profile': profile,
    }

    return render(request, 'users/profile.html', context)
