from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')
