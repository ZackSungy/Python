from django.conf.urls import url

import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$',views.article,name='article'),
    url(r'^edit/html/(?P<article_id>[0-9]+)/$',views.edit_html,name='edit_html'),
    url(r'^edit/$',views.edit_action,name='edit_action'),
]
