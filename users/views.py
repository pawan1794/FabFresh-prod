from django.http import HttpResponse
from django.contrib.auth import login
from social.apps.django_app.utils import psa
from .tools import get_access_token
import json
import requests

from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import UserSerializer,UserInfoSerializer
from .models import UserInfo
from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #http_method_names = ['get', 'put', 'head' ,'patch']
    permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    #queryset = UserInfo.objects.all()
    permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserInfo.objects.all()
        else:
            return UserInfo.objects.filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)


@psa('social:complete')
def register_by_access_token(request, backend):

    token = request.GET.get('access_token')
    number = request.GET.get('number')
    email = request.GET.get('email')

    try:
        user = request.backend.do_auth(token)
        if user:
            login(request, user)
            if email:
                u = User.objects.get(id = user.id)
                u.email = email
                u.save()
            return get_access_token(user)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return HttpResponse("Error",status=status.H)


class CheckAvailabilityApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request, *args, **kw):
        payload = request.data
        url = 'http://roadrunnr.in/v1/orders/serviceability'
        headers = {'Authorization' : 'Bearer HQ0FoVxzj292CZxSOVVZCRTwJ6QgThcmNy56RJ04' , 'Content-Type' : 'application/json'}
        r = requests.post(url, json.dumps(payload), headers=headers)
        response = Response(r.json(),status=status.HTTP_200_OK)
        return response
