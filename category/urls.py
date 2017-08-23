from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CategoryList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
]

