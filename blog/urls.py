from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^hola/(?P<a>[0-9]+)/$', views.hola, name='hola'),
    url(r'^post/new', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),    
]