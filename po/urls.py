from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PoList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.PoDetail.as_view()),
]