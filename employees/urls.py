from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^select_datas/$',views.select_datas,name='select_datas'),
    url(r'^select_datas/([0-9]+)$',views.select_datas,name='select_datas')


]