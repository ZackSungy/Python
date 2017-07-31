from django.conf.urls import url

import views
from models import Business

urlpatterns = [
    url(r'^Home/',views.Home,name='Home'),
    url(r'^Order/(?P<Business_num>[0-9]+)',views.Order,name='Order'),
    url(r'^chioce/', views.chioce,name='chioce'),
    url(r'^Bill/', views.Bill, name='Bill'),
    url(r'^Bills/', views.Bills,name='Bills'),
]