"""feed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from feedapp.views import *
urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name="logout"),
    path('reports/', reports, name='reports'),
    path('delete_post/<post_id>', delete_post, name='delete_post'),
    path('report_post/<post_id>', report_post, name='report_post'),
    path('hide_post/<post_id>', hide_post, name='hide_post'),
    path('block_user/<user_id>', block_user, name='block_user'),
    path('', include('social_django.urls')),
    path('admin/', admin.site.urls),
]
