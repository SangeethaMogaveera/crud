from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ClientList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ClientDetail.as_view()),
]