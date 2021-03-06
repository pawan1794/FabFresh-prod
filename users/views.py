from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import login
from social.apps.django_app.utils import psa
from .tools import get_access_token
import json
import requests
from django.http import JsonResponse

from rest_framework import permissions,generics
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication

from django.contrib.auth.models import User
from .serializers import UserSerializer,UserInfoSerializer,AllInOneSeriallizer, UserProfileSerializer, PostalCodeSerializer, SignUpSerializer, LoginSerializer, ChangePasswordSerializer,AndroidAppVersionSerializer, NotificationBoardSerializer
from .models import UserInfo, UserProfile, PostalCode, AndroidAppVersion, NotificationBoard, AllInOne
from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly, IsAuthenticatedOrCreate
from django.conf import settings
import logging
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from rest_framework.decorators import detail_route, list_route
from allauth.account.forms import ResetPasswordForm
from django.utils import timezone

class AllInOneViewSet(viewsets.ModelViewSet):
    queryset = AllInOne.objects.all()
   # permission_classes = [permissions.AllowAny]
    #http_method_names = ['get',]
    serializer_class = AllInOneSeriallizer

class NotificationBoardViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get',]
    serializer_class = NotificationBoardSerializer

    def get_queryset(self):
        return NotificationBoard.objects.filter(notification_valid_until_time__gte = timezone.now())


class AndroidAppVersionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get',]
    queryset = AndroidAppVersion.objects.all()
    serializer_class = AndroidAppVersionSerializer

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

    @list_route(methods=['post'], url_path='change-password',permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request, pk=None):
        try:
            print "asd"
            print request.data
            serializer = ChangePasswordSerializer(data=request.data)
            print "Asd"
            if serializer.is_valid():
                user = request.user
                print user.check_password(request.data['password'])
                if user.check_password(request.data['password']):
                    if request.data['new_password'] == request.data['confirm_password']:
                        user.set_password(request.data['new_password'])
                        user.save()
                        return JsonResponse({'status':'Password Change Successfully'}, status = status.HTTP_200_OK)
                    else:
                        return JsonResponse({'status':'New Password mismatch'}, status = status.HTTP_200_OK)
                        #data = {'detail': 'New Password mismatch'}
                else:
                    return JsonResponse({'status':'Please enter your correct password!'}, status = status.HTTP_200_OK)
                    #data = {'detail': 'Please enter your correct password!'}
        except Exception as e:
            data = {'detail': 'Unable to change password'}
        return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'],url_path='reset-password', permission_classes=[permissions.AllowAny])
    def recover_password(self, request):
        if request.data.get('email'):
            form = ResetPasswordForm({'email': request.data.get('email')})
        if form.is_valid():
            form.save(request)
            return Response("reset password sent to email", status=status.HTTP_400_BAD_REQUEST)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)

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
        statusCode = "Success"
        if otp is not None and userInfo.otp is not None:
            if int(otp) == int(userInfo.otp):
                code = "Verified"
                userInfo.flag = True
                userInfo.save()
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



    if User.objects.filter(username = email).count() :
        data  = "Phone number already registered"
        if UserInfo.objects.filter(phone = phone,flag = True).count() :
            return JsonResponse({'status':data}, status = status.HTTP_200_OK)
        data = "Email already taken"
        return JsonResponse({'status':data}, status = status.HTTP_200_OK)


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
        #if len(r.json()) < 4 :
        #    serviceAv.delay(payload)
        response = Response(r.json(),status=status.HTTP_200_OK)
        return response

#new change for login
class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny,]

    def create(self, request, *args, **kwargs):
        request.data['username'] = request.data['email']
        serializer = self.get_serializer(data=request.data)
        print request.data['phone']
        print UserInfo.objects.filter(phone= int(request.data['phone']),flag = True)
        data  = "Phone number already registered"
        print UserInfo.objects.filter(phone = request.data['phone'],flag = True).count()
        if UserInfo.objects.filter(phone = request.data['phone'],flag = True).count() :
            return JsonResponse({'status':data}, status = status.HTTP_200_OK)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        userInfo = UserInfo.objects.get(owner = User.objects.get(email = request.data['email']).id)
        userInfo.phone = int(request.data['phone'])
        userInfo.save()
        u = User.objects.get(id = User.objects.get(email = request.data['email']).id)
        return get_access_token(u,int(request.data['phone']),User.objects.get(email = request.data['email']))

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Login(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny,]
    http_method_names = [ 'post',]

    def post(self,request,*args,**kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return get_access_token(user,"","")
        else:
            return Response("Not Authenticated", status=status.HTTP_200_OK)
