from django.conf.urls import url, patterns, include
from . import views
from rest_framework.routers import DefaultRouter
#GCM
from push_notifications.api.rest_framework import GCMDeviceAuthorizedViewSet, APNSDeviceAuthorizedViewSet


router = DefaultRouter()
router.register(r'^info',views.UserViewSet)
router.register(r'^phone',views.UserInfoViewSet,base_name='userinfo')
router.register(r'^device/gcm', GCMDeviceAuthorizedViewSet)
#router.register(r'gcm',GCMDeviceViewSet)
router.register(r'^device/apns', APNSDeviceAuthorizedViewSet)
router.register(r'^address',views.UserProfileViewSet)
router.register(r'^postalcode',views.PostalCodeViewSet)
router.register(r'^appversion',views.AndroidAppVersionViewSet)
router.register(r'^notificationboard',views.NotificationBoardViewSet)

urlpatterns = patterns(
    '',
    url(r'^',
        include(router.urls)),
    url(r'^register-by-token/(?P<backend>[^/]+)/$',
        views.register_by_access_token),
    url(r'^availability/$',
        views.CheckAvailabilityApiView.as_view(), name='my_rest_view'),
    url(r'^otp/$', views.otpVerification.as_view(), name='otpVerification'),
    url(r'^otpresend/$',views.otpResend.as_view(), name='otpresend'),
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    url(r'^login/$', views.Login.as_view(), name="login"),

)
