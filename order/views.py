from rest_framework import viewsets,permissions,status
from .serializers import ordersSerializer
from order.models import orders
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from users.models import UserInfo


def message(self, phone ,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+phone+"&text="+message+"&priority=ndnd&stype=normal"
    r1 = requests.get(url1)



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

        #url = 'http://128.199.241.199/v1/orders/ship'
        url = 'http://roadrunnr.in/v1/orders/ship'
        headers = {'Authorization' : 'Bearer HQ0FoVxzj292CZxSOVVZCRTwJ6QgThcmNy56RJ04' , 'Content-Type' : 'application/json'}
        try:
            print(json.dumps(payload))
            r = requests.post(url, json.dumps(payload), headers=headers)

            if r.status_code == 200:
                response = Response(r.json(),status=status.HTTP_200_OK)
                if flag == 0:
                    order.roadrunner_order_id = r.json()['order_id']
                    order.delivery_id = r.json()['delivery_id']
                    order.save()
                    text_message = "Dear "+payload['pickup']['user']['name']+". Your Order No :"+payload['order_details']['order_id']+" with FabFresh is placed Successfully. Our Logistics Partner will be there to pick up your clothes . Pickup boy details will be sent to you shortly. You can track your order in the app now !"
                    message(self,userInfo[0].phone,text_message)
                if flag == 1:
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
                order.update(amount = 30)
            else:
                order.update(amount = 40)
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
