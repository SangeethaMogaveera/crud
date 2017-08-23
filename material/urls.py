from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MaterialList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.MaterialDetail.as_view()),
]

