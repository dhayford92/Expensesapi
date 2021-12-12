from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_fields = ['fullname', 'email', 'is_staff']
    search_field = ['fullname', 'email']
    filter_fields = ['last_login']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)