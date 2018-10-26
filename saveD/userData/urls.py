from django.conf.urls import url

from . import views

urlpatterns = [
   # url('', views.index, name='index'),
    url(r'^customers/$',views.customerList),
    url(r'^customers/(?P<name>[\w.@+-]+)/$',views.customerDetails),
    url(r'^customers/favs/(?P<name>[\w.@+-]+)/$',views.customerFavouriteDetails),
    url(r'^customers/search/(?P<name>[\w.@+-]+)/$', views.customerSearchDetails),
    url(r'^customers/markSafe/(?P<name>[\w.@+-]+)/$', views.marksafe),
    url(r'^customers/markUnsafe/(?P<name>[\w.@+-]+)/$', views.markunsafe),

]