from django.conf.urls import url

from . import views

urlpatterns = [
   # url('', views.index, name='index'),
    url(r'^customers/$',views.customerList),
    url(r'^customers/(?P<name>[\w.@+-]+)/$',views.customerDetails)
]