from rest_framework import routers
from django.conf.urls import patterns,url,include
from . import views

router = routers.DefaultRouter()
router.register(r'orders',views.ordersViewSet,)
router.register(r'cloth/color',views.ColorViewSet)
router.register('cloth/brand',views.BrandViewSet)
router.register('cloth/type',views.TypeViewSet)
router.register('cloth/size',views.SizeViewSet)
router.register('cloth/cloths',views.ClothViewSet)
router.register('cloth/info',views.ClothInfoViewSet)
router.register('drive/info',views.DriverDetailsViewSet)
router.register('order/status',views.StatusTimeStampViewSet)

urlpatterns = patterns(
    '',
    url(r'^',
        include(router.urls)),
    url(r'^placeorder/$',
        views.PlaceOrderShipment.as_view(), name='place_order'),
    url(r'^track/$',views.Track.as_view(),name='track'),
    url(r'^callback/$',views.CallBackApiView().as_view(),name='callBack'),
    url(r'^setAmount/$' , views.setPrice.as_view(), name='setPrice'),
    url(r'^cancel/$', views.OrderCancel.as_view(), name = 'CancelOrder'),
    url(r'^aboutus/$' , views.AboutUs.as_view(), name='AboutUs'),
    url(r'^faq/$', views.Faq.as_view(), name='FaQ'),
    url(r'^deletegcm/$',views.deleteGCM.as_view(),name='deleteGCM'),
    url(r'^coupons/$',views.CouponView.as_view(),name='coupon')
)