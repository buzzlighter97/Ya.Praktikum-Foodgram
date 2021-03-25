from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from users.forms import RegistrationForm


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            return render(
                request,
                'registration/registration.html',
                {'form': form}
            )
    form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('login')
    success_message = "Вы успешно зашли!"
