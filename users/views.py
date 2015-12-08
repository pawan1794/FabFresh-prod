from django.core.mail import send_mail
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
from .serializers import UserSerializer,UserInfoSerializer, UserProfileSerializer
from .models import UserInfo, UserProfile
from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly
from django.conf import settings


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserProfile.objects.all()
        else:
            return UserProfile.objects.filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)


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
    phone = request.GET.get('phone')
    email = request.GET.get('email')

    try:

        user = request.backend.do_auth(token)
        print "asd"
        if user:
            login(request, user)
            u = User.objects.get(id = user.id)

            if email:
                u.email = email
                u.save()
            '''
            if phone:

                #NEW
                up = UserProfile.objects.get(user = user.id)

                if not up.phone:
                    userProfile = UserProfile(user = u)
                    userProfile.phone = phone
                    userProfile.save()
                    #OLD
                userInfo = UserInfo(owner=u)
                userInfo.phone = phone
                userInfo.save()
            '''
            return get_access_token(user,phone,email)
        else:
            return Response("asd",status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return HttpResponse(e,status=status.HTTP_404_NOT_FOUND)


class CheckAvailabilityApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request, *args, **kw):
        payload = request.data
        url = 'http://roadrunnr.in/v1/orders/serviceability'
        headers = {'Authorization' : 'Bearer HQ0FoVxzj292CZxSOVVZCRTwJ6QgThcmNy56RJ04' , 'Content-Type' : 'application/json'}
        r = requests.post(url, json.dumps(payload), headers=headers)
        response = Response(r.json(),status=status.HTTP_200_OK)
        return response

