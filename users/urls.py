from django.contrib.auth import views as auth_views
from django.urls import include, path

from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logout.html'), name='logout'),
    path(
        'password-change/done/', auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'
        ), name='password_change_done'),
    path('', include('django.contrib.auth.urls')),

]
