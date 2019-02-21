from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^hola/(?P<a>[0-9]+)/$', views.hola, name='hola'),
]