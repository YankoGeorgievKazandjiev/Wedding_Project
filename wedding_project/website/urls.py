from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='registerView'),
    url(r'^help/$', views.help, name='help'),
]
