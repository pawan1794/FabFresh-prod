
from rest_framework import viewsets,permissions,status
from .serializers import ordersSerializer
from order.models import orders
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from users.models import UserInfo
from .models import Color,Type,Size, ClothInfo
from .serializers import  ColorSerializer,\
    TypeSerializer,\
    SizeSerializer,\
    ClothInfoSerializer,\
    ClothInforamtionSerializer,\
    ClothsOrdersSerializer
from gcm import *

def message(self, phone ,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+phone+"&text="+message+"&priority=ndnd&stype=normal"
    r1 = requests.get(url1)



class ordersViewSet(viewsets.ModelViewSet):
    serializer_class = ordersSerializer
    queryset = orders.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return orders.objects.all()
        else:
            return orders.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except Exception as e:
            return Response(e,status=status.HTTP_404_NOT_FOUND)

    '''def update(self, request, *args, **kwargs):
        for i in request.data:
            if str(i) == "status":
                order = orders.objects.filter(id = kwargs['pk'])
                userInfo = UserInfo.objects.filter(owner = self.request.user)
                if int(request.data['status']) is 6 :
                    text_message = "Dear "+ str(self.request.user) +" , Your Order is packed and Ready for Delivery . Please Select Deliver Now in the app to get it at your doorstep. "
                    message(self,userInfo[0].phone, text_message)

        return super(ordersViewSet, self).update(request, *args, **kwargs)
    '''
class PlaceOrderShipment(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'put', 'head' ,'patch','post']
    def post(self,request, *args, **kw):
        flag = 0
        payload = request.data

        print type(payload['order_details']['order_id'])
        if int(payload['order_details']['order_id']) is 0:
            try:
                order = orders(owner=self.request.user)
                order.special_instructions = payload['special_instructions']
                order.order_type = payload['order_type']
                order.save()
                payload['order_details']['order_id'] = unicode(order.id)
            except Exception as e:
                return Response(e,status=status.HTTP_404_NOT_FOUND)
        else:
            flag = 1
            order = orders.objects.filter(id = payload['order_details']['order_id'])

        userInfo = UserInfo.objects.filter(owner = self.request.user)
        print(userInfo[0].phone)
        if flag == 1:
            payload['pickup']['user']['name'] = "FabFresh"
            payload['pickup']['user']['phone_no'] = "09066093765"
            payload['pickup']['user']['email'] = "fabfresh.in"
            payload['pickup']['user']['type'] = "merchant"
            payload['pickup']['user']['external_id'] = "1002"
            payload['pickup']['user']['full_address']['address'] = "#67, 2nd Floor,7th cross,Near Police Station"
            payload['pickup']['user']['full_address']['locality']['name'] = "Wilson Garden"
            payload['pickup']['user']['full_address']['city']['name'] = "Bangalore"
            payload['pickup']['user']['full_address']['geo']['latitude'] = "12.943834"
            payload['pickup']['user']['full_address']['geo']['longitude'] = "77.623928"
        if flag == 0:
            payload['drop']['user']['name'] = "FabFresh"
            payload['drop']['user']['phone_no'] = "09066093765"
            payload['drop']['user']['email'] = "fabfresh.in"
            payload['drop']['user']['type'] = "merchant"
            payload['drop']['user']['external_id'] = "1002"
            payload['drop']['user']['full_address']['address'] = "#67, 2nd Floor,7th cross,Near Police Station"
            payload['drop']['user']['full_address']['locality']['name'] = "Wilson Garden"
            payload['drop']['user']['full_address']['city']['name'] = "Bangalore"
            payload['drop']['user']['full_address']['geo']['latitude'] = "12.943834"
            payload['drop']['user']['full_address']['geo']['longitude'] = "77.623928"

        #url = 'http://128.199.241.199/v1/orders/ship'
        url = 'http://roadrunnr.in/v1/orders/ship'
        headers = {'Authorization' : 'Bearer HQ0FoVxzj292CZxSOVVZCRTwJ6QgThcmNy56RJ04' , 'Content-Type' : 'application/json'}
        try:
            print(json.dumps(payload))

            r = requests.post(url, json.dumps(payload), headers=headers)
            print(r.status_code)
            if r.status_code == 200:

                response = Response(r.json(),status=status.HTTP_200_OK)
                if flag == 0:
                    order.roadrunner_order_id = r.json()['order_id']
                    order.delivery_id = r.json()['delivery_id']
                    order.save()
                    text_message = "Dear "+payload['pickup']['user']['name']+". Your Order No :"+payload['order_details']['order_id']+" with FabFresh is placed Successfully. Our Logistics Partner will be there to pick up your clothes . Pickup boy details will be sent to you shortly. You can track your order in the app now !"
                    message(self,userInfo[0].phone,text_message)
                if flag == 1:
                    pass
                    text_message = "Dear "+payload['drop']['user']['name']+". Your Order No :"+payload['order_details']['order_id']+"  is on its way. Delivery Boy details will be sent to you shortly. Once again , Thanks for using FabFresh. Please provide your feedback in the app . Have a Wonderful day ! "
                    message(self,userInfo[0].phone,text_message)
                return response
            else:
                order.delete()
                return Response(r.json(),status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response( e,status=status.HTTP_404_NOT_FOUND)



class OrderCancel(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kw):
        payload = request.data

        try:
            order = orders.objects.filter(id = payload['id'])
        except Exception as e:
            return Response(e,status=status.HTTP_204_NO_CONTENT)

        url = "http://roadrunnr.in/v1/orders/"+ payload['id'] +"/cancel"
        headers = {'Authorization' : 'Bearer HQ0FoVxzj292CZxSOVVZCRTwJ6QgThcmNy56RJ04' , 'Content-Type' : 'application/json'}
        try:
            r = requests.get(url , headers=headers)
            if r.status_code == 200:
                order.update(status = 0)
                return Response("Order Cancelled" , status=status.HTTP_200_OK)
            else:
                return Response("Order Not Cancelled" , status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e , status = status.HTTP_404_NOT_FOUND)


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
            print(j)
        url = "http://128.199.241.199/v1/orders/" + j + "/track"
        headers = {'Authorization' : 'Bearer 4RaJAmtaOEfHJu1dkyWIUVGmckcTizGXyyxPFIgy' , 'Content-Type' : 'application/json'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            response = Response(r.json(), status=status.HTTP_200_OK)
            return response


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
            try:
                order = orders.objects.filter(id = payload['id'])
            except Exception as e:
                return Response(e ,status = status.HTTP_404_NOT_FOUND)

            order.update(quantity = payload['quantity'])
            order.update(weight = float(payload['weight']))
            order.update(status = payload['status'])


            a = str(order[0].created_at_time)
            print a
            a = a[-10:]
            if int(a[1]) == 0:
                a = int(a) + 1000
                a = str(a)
            order.update(p_id = a[:4])

            if order[0].order_type == 1:
                order.update(amount = 0)
            else:
                order.update(amount = 0)
            try:
                order = orders.objects.filter(id = payload['id'])
                for i in order:
                    print i.owner
                userInfo = UserInfo.objects.filter(owner = i.owner)
                phone = 0
                name = " "
                for i in userInfo:
                    phone = i.phone
                    name = i.owner

                #userInfo = UserInfo.objects.filter(owner = self.request.user)
                text_message = "Dear "+ str(name) +" , Your Order No : "+ str(payload['id']) +". Number of Clothes : "+ str(order[0].quantity) +" , Weight : "+ str(order[0].weight) +" KG , Price : "+ str(order[0].amount) +" .We have started processing your clothes. You can check the status of processing (like Washing , Drying , Ironing , Packaging ) in the app now !  "
                message(self,phone, text_message)
            except Exception as e:
                return Response(userInfo[0].phone+userInfo+"SMS Not Sent" ,status = status.HTTP_404_NOT_FOUND)

            gcm = GCM("AIzaSyALq9M9qOYsu7Nqm0KQOJXCwCrtODif0ig")
            data = {'The_message' : 'you have x new friends','param2':'value1'}
            reg_id = 'APA91bEpgPjHmT0mA9YPwXvRFPTuHQr9U0mKCWmg4eBWdE3kefaFlGxt0xChLtOpBI9IKqwefKI3ahAfZPZ0b4p-0kLVrbsXBa86ro7aVmdGbE5XdqKVuakbI4PwfX4JX_995k8fk8i4ix2O3zIz0fhkfkzK3mKqmQ'
            gcm.plaintext_request(registration_id=reg_id, data=data)
        except Exception as e:
            return Response(e ,status = status.HTTP_404_NOT_FOUND)
        return Response("Success" , status = status.HTTP_200_OK)



class CallBackApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request, *args, **kw):
        payload = request.data
        print(payload)
        return Response("Success", status=status.HTTP_200_OK)


class AboutUs(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self , request, *args , **kw):
        payload = {
            "About Us" : "FabFresh Is KickAss"
        }
        return Response(payload , status=status.HTTP_200_OK)


class Faq(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kw):
        payload = {
            "What is this" : "Fab FResh it is",
            "Another question" : "New Ans"
        }
        return  Response(payload, status=status.HTTP_200_OK)

class ColorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class TypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class SizeViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ClothViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = ClothInfo.objects.all()
    serializer_class = ClothInfoSerializer

class ClothInfoViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = ClothInfo.objects.all()
    serializer_class = ClothInforamtionSerializer
