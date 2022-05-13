from dataclasses import field
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    can_delete = False
    model = Profile

# class UserAdmin(admin.ModelAdmin):
    # inlines = [ProfileInline]
    # exclude = ['groups','first_name','last_name','user_permissions']
    # fields = ['username','password']

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Profile)