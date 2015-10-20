from rest_framework import viewsets,permissions,status
from .serializers import ordersSerializer
from order.models import orders
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import os

class ordersViewSet(viewsets.ModelViewSet):
    serializer_class = ordersSerializer
    queryset = orders.objects.all()
    #permission_classes = [permissions.IsAuthenticated,TokenHasReadWriteScope]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return orders.objects.all()
        else:
            return orders.objects.filter(owner = self.request.user.id)

    def perform_create(self, serializer):
        print(self.request.user)
        try:
            serializer.save(owner=self.request.user)
        except Exception as e:
            return Response(e,status=status.HTTP_404_NOT_FOUND)

class PlaceOrderShipment(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'put', 'head' ,'patch','post']
    def post(self,request, *args, **kw):
        payload = request.data
        #payload['order_details']['order_id']
        #createOrder(payload['order_details'])
        try:
            order = orders(owner=self.request.user)
            order.save()
        except Exception as e:
            return Response(e,status=status.HTTP_404_NOT_FOUND)

        #add data to json
        payload['order_details']['order_id'] = unicode(order.id)

        #url = 'http://128.199.241.199/v1/orders/ship'
        url = 'http://roadrunnr.in/v1/orders/ship'
        headers = {'Authorization' : 'Bearer HQ0FoVxzj292CZxSOVVZCRTwJ6QgThcmNy56RJ04' , 'Content-Type' : 'application/json'}
        try:
            print(json.dumps(payload))
            r = requests.post(url, json.dumps(payload), headers=headers)

            if r.status_code == 200:
                response = Response(r.json(),status=status.HTTP_200_OK)
                order.roadrunner_order_id = r.json()['order_id']
                order.delivery_id = r.json()['delivery_id']

                #enter special instructions details and order_type for order before save
                order.save()
                return response
            else:
                return Response(r.json(),status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response( e,status=status.HTTP_404_NOT_FOUND)


class Track(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request, *args, **kw):
        payload = request.data
        order_id = int(payload['id'])
        roadrunner_order_id = orders.objects.filter(id = order_id)
        print(roadrunner_order_id)
        j = "asd"
        for i in roadrunner_order_id:
            j = str(i.id)
        url = "http://128.199.241.199/v1/orders/" + j + "/track"
        headers = {'Authorization' : 'Bearer 4RaJAmtaOEfHJu1dkyWIUVGmckcTizGXyyxPFIgy' , 'Content-Type' : 'application/json'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            response = Response(r.json(), status=status.HTTP_200_OK)
            return response

class CancelOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kw ):
        payload = request.data
        url = 'http://roadrunnr.in/v1/orders/ship'
        headers = {'Authorization' : 'Bearer HQ0FoVxzj292CZxSOVVZCRTwJ6QgThcmNy56RJ04' , 'Content-Type' : 'application/json'}
        try:
            print(json.dumps(payload))
            r = requests.post(url, json.dumps(payload), headers=headers)
            if r.status_code == 200:
                response = Response(r.json(),status=status.HTTP_200_OK)
                order.roadrunner_order_id = r.json()['order_id']
                order.delivery_id = r.json()['delivery_id']

                #enter special instructions details and order_type for order before save
                order.save()
                return response
            else:
                return Response(r.json(),status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response( e,status=status.HTTP_404_NOT_FOUND)


class setPrice(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return orders.objects.all()
        else:
            return orders.objects.filter(owner=self.request.user.id)

    def post(self, request, *args,**kw):
        try:
            payload = request.data

            #order = orders.objects.filter(id = request.data.id)
            print order
            print payload
        except Exception as e:
            return Response(e ,status = status.HTTP_404_NOT_FOUND)
        return Response("Success" , status = status.HTTP_200_OK)


class CallBackApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request, *args, **kw):
        payload = request.data
        print(payload)
        return Response("Success", status=status.HTTP_200_OK)


class SpecialInstructions(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        payload = {
            "instructions":{
                "1" : "Wassup",
                "2" : "Go",
                "3" : "Beep",
                "4":"youself"
            }
        }
        return Response(payload, status=status.HTTP_200_OK)


