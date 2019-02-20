from . import views
from django.conf.urls import url, include

urlpatterns = [
    url('', views.post_list, name='post_list'),
]