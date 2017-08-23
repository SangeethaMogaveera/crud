from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ConsultantList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ConsultantDetail.as_view()),
]