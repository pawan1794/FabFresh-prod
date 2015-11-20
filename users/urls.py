from django.conf.urls import url, patterns, include
from . import views
from rest_framework.routers import DefaultRouter
#GCM
from push_notifications.api.rest_framework import GCMDeviceAuthorizedViewSet


router = DefaultRouter()
router.register(r'info',views.UserViewSet)
router.register(r'^userinfo',views.UserInfoViewSet,base_name='userinfo')
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)
#router.register(r'gcm',GCMDeviceViewSet)

urlpatterns = patterns(
    '',
    url(r'^',
        include(router.urls)),
    url(r'^register-by-token/(?P<backend>[^/]+)/$',
        views.register_by_access_token),
    url(r'^availability/$',
        views.CheckAvailabilityApiView.as_view(), name='my_rest_view'),
)
