
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from django.conf import settings


admin.site.site_header = settings.APP_SITE_HEADER
admin.site.site_title = settings.APP_SITE_TITLE
admin.site.index_title = settings.APP_INDEX_TITLE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/admin')),
]
