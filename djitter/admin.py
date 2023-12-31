from django.contrib import admin
from django.contrib.auth.models import User, Group

from djitter.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    models = User
    fields = ['username']
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
