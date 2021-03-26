from django.contrib import admin, auth

from users.models import User


class Admin(auth.admin.UserAdmin):
    list_filter = ('username', 'email',)
    search_fields = ('^username', '^email',)
    ordering = ('username',)


admin.site.register(User, Admin)
admin.site.unregister(auth.models.Group)
