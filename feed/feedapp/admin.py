from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Report, User
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Report)