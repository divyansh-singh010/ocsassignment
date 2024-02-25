from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'role')
    search_fields = ('userid', 'role')


admin.site.register(User, UserAdmin)
