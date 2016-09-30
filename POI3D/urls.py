from django.conf.urls import url

from . import views

app_name = '3DPOI'
urlpatterns = [url(r'^$', views.index, name= 'index'),
               #url(r'^(?P<processor_id>[0-9]+)/$', views.detail, name='detail'),
               #url(r'^(?P<processor_id>[0-9]+)/corecaller/$', views.corecaller, name='corecaller'),
               #url(r'^(?P<processor_id>[0-9]+)/result/$', views.result, name='result'),
               ]
