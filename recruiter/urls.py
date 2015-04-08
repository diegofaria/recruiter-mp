from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.candidate_new, name='candidate_new'),
    url(r'^candidate/list/$', views.candidate_list, name='candidate_list'),
    url(r'^candidate/(?P<pk>[0-9]+)/$', views.candidate_detail),
    url(r'^candidate/(?P<pk>[0-9]+)/edit/$', views.candidate_edit, name='candidate_edit'),
]
