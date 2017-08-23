from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SubCategoryList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SubCategoryDetail.as_view()),
]

