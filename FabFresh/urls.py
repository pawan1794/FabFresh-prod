from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^users/', include('users.urls')),
    url(r'^', include('order.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
