from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BrandList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BrandDetail.as_view()),
]

