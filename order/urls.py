from rest_framework import routers
from django.conf.urls import patterns,url,include
from . import views

router = routers.DefaultRouter()
router.register(r'orders',views.ordersViewSet,)

urlpatterns = patterns(
    '',
    url(r'^',
        include(router.urls)),
    url(r'^placeorder/$',
        views.PlaceOrderShipment.as_view(), name='place_order'),
    url(r'^track/$',views.Track.as_view(),name='track'),
    url(r'^callback/$',views.CallBackApiView().as_view(),name='callBack'),
    url(r'^setAmount/$' , views.setPrice.as_view(), name='setPrice'),
    url(r'^cancel/$', views.OrderCancel.as_view(), name = 'CancelOrder')
)