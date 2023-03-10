
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/admin')),
]
