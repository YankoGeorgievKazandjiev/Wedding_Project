from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='registerView'),
    url(r'^help/$', views.help, name='help'),
    # url(r'^guests/$', views.GuestListView.as_view(), name='GuestListView'),
    url(r'^present/$', views.PresentListView.as_view(), name='present'),

    # url(r'^PresentSaveView$', views.PresentSaveView.as_view(), name='PresentSaveView'),
    url(r'^present/create', views.PresentCreateView.as_view(), name='create-present'),
    url(r'^present/update/(?P<pk>[0-9]+)/$', views.ReserveView.as_view(), name='update-present'),
]
