from django.contrib import admin
from django.contrib.auth.models import User, Group


class UserAdmin(admin.ModelAdmin):  # type: ignore
    models = User
    fields = ['username']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
