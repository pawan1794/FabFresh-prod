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
    url(r'^track/$',views.Track.as_view(),name='track')
)