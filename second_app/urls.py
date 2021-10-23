from django.conf.urls import url
from second_app import views

urlpapperns=[
    url(r'^$',views.index, name='index'),
    url(r'^$',views.helping,name='help')
]