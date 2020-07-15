#from django.urls import path
from django.conf.urls import url

from . import views

'''urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(\d+)/$', views.sz, name='sz'),
]'''
urlpatterns=[
    url(r'^$', views.index),
    url(r'-?[1-9]\d*',views.sz),
    url(r'^grades/$',views.grades),
    url(r'^students/$', views.students),

]