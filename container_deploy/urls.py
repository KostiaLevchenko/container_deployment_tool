from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^run/another/container/$', views.run_another_container, name='run_another_container'),
    url(r'^images/all$', views.images_list, name='images_list'),
    url(r'^containers/all$', views.containers_list, name='containers_list'),
]