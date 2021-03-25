from django.conf.urls import handler404, handler500  # noqa
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include, path

handler404 = 'recipes.views.page_not_found' # noqa
handler500 = 'recipes.views.server_error' # noqa

urlpatterns = [
    path('', include('recipes.urls')),
    path('', include('users.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('profile/', include('django.contrib.flatpages.urls')),
    path('about/', views.flatpage, {'url': '/profile/about/'}, name='about'),
    path(
        'technologies/',
        views.flatpage,
        {'url': '/profile/portfolio/'},
        name='technologies'
    ),
]
