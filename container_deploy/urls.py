from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.containers_list, name='containers_list'),
    # url(r'^container/(?P<pk>[0-9]+)/$', views.container_detail, name='container_detail'),
    # url(r'^run/container/$', views.run_container, name='run_container'),
    url(r'^run/another/container/$', views.run_another_container, name='run_another_container'),
    url(r'^containers/all$', views.containers_list, name='containers_list'),
]