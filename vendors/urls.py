from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.VendorList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.VendorDetail.as_view()),
]