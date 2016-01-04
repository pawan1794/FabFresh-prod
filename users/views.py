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
from .serializers import UserSerializer,UserInfoSerializer, UserProfileSerializer, PostalCodeSerializer
from .models import UserInfo, UserProfile, PostalCode
from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly
from django.conf import settings
import logging



class PostalCodeViewSet(viewsets.ModelViewSet):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer

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

class otpVerification(APIView):

    def get(self, request, *args, **kw):
        '''userInfo = UserInfo.objects.get(owner = self.request.user.id)
        print userProfile.opt
        '''
        otp = request.GET.get('otp')
        userInfo = UserInfo.objects.get(owner = self.request.user.id)
        statusCode = "Sucess"
        if otp is not None and userInfo.otp is not None:
            if int(otp) == int(userInfo.otp):
                code = "Verified"
            else:
                code = "Not Verified"
        payload = {
            "Status" : code
        }
        return Response(payload, status=status.HTTP_200_OK)
import random
from .tools import message

class otpResend(APIView):
    def get(self,request,*args,**kw):
        code = "default"

        userInfo = UserInfo.objects.get(owner = self.request.user.id)
        if userInfo is None:
            code = "No user data"
            payload = {
                "status" : code
            }
            return Response(payload, status=status.HTTP_200_OK)
        #OTP
        otp = random.randint(10000,1000000)
        OTP_text_message = "OTP:"+ str(otp) + ". Use the above OTP to verify you mobile number on FabFresh"
        try:
            message(userInfo.phone,OTP_text_message)
        except Exception as e:
            code = "message not sent"
            payload = {
                "status" : code
            }
        userInfo.otp = otp
        userInfo.save()
        code = "success"
        payload = {
            "status" : code
        }
        return Response(payload, status=status.HTTP_200_OK)


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
            return get_access_token(user,phone,email)
        else:
            return Response("asd",status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return HttpResponse(e,status=status.HTTP_404_NOT_FOUND)

from FabFresh.task import serviceAv

class CheckAvailabilityApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request, *args, **kw):
        payload = request.data
        #serviceAv.delay(payload)
        url = 'http://roadrunnr.in/v1/orders/serviceability'
        headers = {'Authorization' : 'Bearer L0vqwtrFUodi6VA8HhxKtSdVjTinUUaoHEUk2VPP' , 'Content-Type' : 'application/json'}
        r = requests.post(url, json.dumps(payload), headers=headers)
        if len(r.json()) < 4 :
            serviceAv.delay(payload)
        response = Response(r.json(),status=status.HTTP_200_OK)
        return response

