from django.conf.urls import url
from django.contrib.auth.views import login, logout
import os
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'home'

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^add', views.add, name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
