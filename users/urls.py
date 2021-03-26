from django.contrib.auth import views as auth_view
from django.urls import path

from users import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        auth_view.LoginView.as_view(
            template_name='authForm.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_view.LogoutView.as_view(
            template_name='logged_out.html'
        ),
        name='logout'
    ),
    path(
        'password_change/',
        auth_view.PasswordChangeView.as_view(
            template_name='changePassword.html'
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_view.PasswordChangeDoneView.as_view(
            template_name='password_change_done.html'
        ),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        auth_view.PasswordResetView.as_view(
            template_name='resetPassword.html'
        ),
        name='password_reset'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_view.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    path(
        'password_reset/done/',
        auth_view.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),
]
