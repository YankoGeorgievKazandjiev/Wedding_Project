from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='registerView'),
    url(r'^help/$', views.help, name='help'),
    # url(r'^guests/$', views.GuestListView.as_view(), name='GuestListView'),
    url(r'^present/$', views.PresentListView.as_view(), name='present'),
    url(r'^admin_page$', views.AdminView.as_view(), name='AdminView'),
]
