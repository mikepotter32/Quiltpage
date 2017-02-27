from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views
app_name = 'home'

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^add', views.add, name='add'),

]
