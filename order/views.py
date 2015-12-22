from django.http import JsonResponse
from rest_framework import viewsets,permissions,status
from .serializers import ordersSerializer
from order.models import orders
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from users.models import UserInfo
from .models import Color, Type, Size, ClothInfo, DriverDetails, Brand
from .serializers import ColorSerializer, \
    TypeSerializer, \
    SizeSerializer, \
    ClothInfoSerializer, \
    ClothInforamtionSerializer, \
    ClothsOrdersSerializer, \
    DriverDetailsSerializer, \
    BrandSerializer
from gcm import *
from push_notifications.models import GCMDevice,APNSDevice
import datetime
from django.utils.timezone import utc
from random import randint
import math
from django.utils import timezone

def message(self, phone ,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+phone+"&text="+message+"&priority=ndnd&stype=normal"
    r1 = requests.get(url1)

def gcm(self, owner_id,order_id,status):
    reg_id = GCMDevice.objects.filter(user_id = owner_id)
    try:
        gcm_reg_id = reg_id[0].registration_id
        device = GCMDevice.objects.get(registration_id = gcm_reg_id)
        try:
            device.send_message( str(order_id) + " " +str(status) )
        except Exception as e:
            print e
    except Exception as e:
        print e

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    print c*r
    return (c*r)

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
            return Response(e, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        print "asd"
        order = orders.objects.filter(id= kwargs['pk'])
        order.update(modified_at_time=timezone.now())
        print order
        for i in order:
            print i.owner
            i.modified_at_time=timezone.now()
        owner = i.owner
        userInfo = UserInfo.objects.filter(owner = i.owner)
        for j in userInfo:
            phone = j.phone

        gcm(self,j.owner_id,kwargs['pk'],request.data['status'])

        for i in request.data:
            if str(i) == "status":
                order = orders.objects.filter(id = kwargs['pk'])

                userInfo = UserInfo.objects.filter(owner = self.request.user)

                if int(request.data['status']) is 6 :
                    text_message = "Dear "+ str(owner) +" , Your Order is packed and Ready for Delivery . Please Select Deliver Now in the app to get it at your doorstep. "
                    message(self,phone, text_message)

        return super(ordersViewSet, self).update(request, *args, **kwargs)


class PlaceOrderShipment(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'put', 'head', 'patch', 'post']

    def post(self, request, *args, **kw):
        now = int(datetime.datetime.now().strftime('%H'))
        #add time details
        flag = 0
        payload = request.data
        payload['callback'] = "http://fabfresh.elasticbeanstalk.com/callback"
        print now
        if now < 20 and now > 9:
            print type(payload['order_details']['order_id'])
            if int(payload['order_details']['order_id']) is 0:
                try:
                    order = orders(owner=self.request.user)
                    order.special_instructions = payload['special_instructions']
                    order.order_type = payload['order_type']
                    order.save()
                    payload['order_details']['order_id'] = unicode(order.id)

                except Exception as e:
                    return Response(e, status=status.HTTP_404_NOT_FOUND)
            else:
                flag = 1
                order = orders.objects.filter(id=payload['order_details']['order_id'])
                if not order:
                    return Response("orderid is not available",status=status.HTTP_200_OK)

            userInfo = UserInfo.objects.filter(owner=self.request.user)

            print(userInfo[0].phone)

            if flag == 1:
                payload['pickup']['user']['name'] = "FabFresh"
                payload['pickup']['user']['phone_no'] = "9108014238"
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
                payload['drop']['user']['phone_no'] = "9108014238"
                payload['drop']['user']['email'] = "fabfresh.in"
                payload['drop']['user']['type'] = "merchant"
                payload['drop']['user']['external_id'] = "1002"
                payload['drop']['user']['full_address']['address'] = "#67, 2nd Floor,7th cross,Near Police Station"
                payload['drop']['user']['full_address']['locality']['name'] = "Wilson Garden"
                payload['drop']['user']['full_address']['city']['name'] = "Bangalore"
                payload['drop']['user']['full_address']['geo']['latitude'] = "12.943834"
                payload['drop']['user']['full_address']['geo']['longitude'] = "77.623928"
                print "asd"
                print haversine(float(payload['pickup']['user']['full_address']['geo']['latitude']),float(payload['pickup']['user']['full_address']['geo']['longitude']),12.948645,77.594783)

                if haversine(float(payload['pickup']['user']['full_address']['geo']['latitude']),float(payload['pickup']['user']['full_address']['geo']['longitude']),12.948645,77.594783) < 4.0:
                    pass
                else:
                    return JsonResponse({'status':'Service Not Available'}, status = status.HTTP_200_OK)
            #url = 'http://128.199.241.199/v1/orders/ship'
            url = 'http://roadrunnr.in/v1/orders/ship'
            headers = {'Authorization' : 'Bearer L0vqwtrFUodi6VA8HhxKtSdVjTinUUaoHEUk2VPP' , 'Content-Type' : 'application/json'}
            try:

                r = requests.post(url, json.dumps(payload), headers=headers)
                if r.status_code == 200:
                    print "Inside 200 status"
                    if r.json()['status']['code'] == 706:
                        if flag == 0:
                            order.delete()
                        response = JsonResponse({"status" : "Delivery Boy Not Available"})
                    else:
                        response = Response(r.json(),status=status.HTTP_200_OK)
                        DriverDetail = DriverDetails(orders_id = payload['order_details']['order_id'],
                                                delivery_id = r.json()['delivery_id'],
                                                driver_name = r.json()['driver_name'],
                                                driver_phone = r.json()['driver_phone'],
                                                order_id = r.json()['order_id'])
                        print "After driver informations stored"
                        if flag == 0:
                            order.roadrunner_order_id = r.json()['order_id']
                            order.delivery_id = r.json()['delivery_id']
                            order.save()
                            DriverDetail.new_trip = True
                            DriverDetail.save()
                            text_message = "Dear " + payload['pickup']['user']['name'] + ". Your Order No :" + \
                                   payload['order_details']['order_id'] + " with FabFresh is placed Successfully. Our Logistics Partner will be there to pick up your clothes . Pickup boy details will be sent to you shortly. You can track your order in the app now !"
                            message(self, userInfo[0].phone, text_message)

                        if flag == 1:
                            order.update(status=7)
                            DriverDetail.new_trip = False
                            DriverDetail.save()
                            text_message = "Dear " + payload['drop']['user']['name'] + ". Your Order No :" + \
                                       payload['order_details'][
                                       'order_id'] + "  is on its way. Delivery Boy details will be sent to you shortly. Once again , Thanks for using FabFresh. Please provide your feedback in the app . Have a Wonderful day ! "
                            message(self, userInfo[0].phone, text_message)
                    print "After message sent "
                    return response

                else:
                    if flag == 0:
                        order.delete()
                    return Response(r.json(), status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response(e, status=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({'status':'Time Up'}, status = status.HTTP_200_OK)

class OrderCancel(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kw):
        payload = request.data

        try:
            order = orders.objects.filter(id=payload['id'])
            print order[0].roadrunner_order_id
        except Exception as e:
            return Response(e, status=status.HTTP_204_NO_CONTENT)

        url = "http://roadrunnr.in/v1/orders/" + order[0].roadrunner_order_id + "/cancel"
        headers = {'Authorization': 'Bearer L0vqwtrFUodi6VA8HhxKtSdVjTinUUaoHEUk2VPP',
                   'Content-Type': 'application/json'}
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                order.update(status=0)
                return JsonResponse({'status':'Order Cancelled'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"status" : "Order Not Cancelled"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND)


class Track(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kw):
        payload = request.data
        order_id = int(payload['id'])
        roadrunner_order_id = orders.objects.filter(id=order_id)
        print(roadrunner_order_id)
        j = "asd"
        for i in roadrunner_order_id:
            j = str(i.id)
            print(j)
        url = "http://roadrunnr.in/v1/orders/" + j + "/track"
        headers = {'Authorization': 'Bearer L0vqwtrFUodi6VA8HhxKtSdVjTinUUaoHEUk2VPP',
                   'Content-Type': 'application/json'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            response = Response(r.json(), status=status.HTTP_200_OK)
            return response

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

class setPrice(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return orders.objects.all()
        else:
            return orders.objects.filter(owner=self.request.user.id)

    def post(self, request, *args, **kw):
        try:
            payload = request.data
            try:
                order = orders.objects.filter(id=payload['id'])
                if not order:
                    return JsonResponse({'status' : 'Order not Avalilable'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response(e, status=status.HTTP_404_NOT_FOUND)

            order.update(quantity=payload['quantity'])
            order.update(weight=float(payload['weight']))
            order.update(status=payload['status'])
            order.update(modified_at_time=timezone.now())
            print timezone.now()
            a = str(order[0].created_at_time)
            print a
            a = a[-10:]
            if int(a[1]) == 0:
                a = random_with_N_digits(4)
                if a < 1000:
                    a = a + 1000
                a = str(a)
                if a < 1000:
                    a = a + 1000
            order.update(p_id=a[:4])

            if order[0].order_type == 1:
                order.update(amount=0)
            else:
                order.update(amount=0)
            try:
                order = orders.objects.filter(id=payload['id'])
                for i in order:
                    print i.owner
                userInfo = UserInfo.objects.filter(owner = i.owner)


                phone = 0
                name = " "
                for i in userInfo:
                    phone = i.phone
                    name = i.owner
                print (i.owner_id)
                # userInfo = UserInfo.objects.filter(owner = self.request.user)
                text_message = "Dear " + str(name) + " , Your Order No : " + str(
                    payload['id']) + ". Number of Clothes : " + str(order[0].quantity) + " , Weight : " + str(
                    order[0].weight) + " KG , Price : " + str(order[0].amount) + " .We have started processing your clothes. You can check the status of processing (like Washing , Drying , Ironing , Packaging ) in the app now !  "
                message(self, phone, text_message)
            except Exception as e:
                return Response(userInfo[0].phone + userInfo + "SMS Not Sent", status=status.HTTP_404_NOT_FOUND)

            '''apns_token = "87f26e125e83985a5b7854098af198f357290152b47d353578e0667b5f89c229"
            try:
                device = APNSDevice.objects.get(registration_id=apns_token)
                device.send_message(str(payload['id']) + " 2")
            except Exception as e:
                print "e"
            '''
            gcm(self,i.owner_id,payload['id'],2)

            '''print i.id
            print "user id" + str(self.request.user.id)
            reg_id = GCMDevice.objects.filter(user_id = i.owner_id)
            print reg_id
            try:
                gcm_reg_id= reg_id[0].registration_id

                device = GCMDevice.objects.get(registration_id=gcm_reg_id)
                try:
                    device.send_message( str(payload['id']) + " 2")
                except Exception as e:
                    print e
            except Exception as e:
                print e
            '''

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND)
        return Response("Success", status=status.HTTP_200_OK)


class CallBackApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kw):
        payload = request.data
        print(payload)
        if payload['status'] == "REACHED_PICKUP":
            text_message = str(payload['status'])
            message(self, "7204680605", text_message)
        return Response("Success", status=status.HTTP_200_OK)

class deleteGCM(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kw):
        GCMDevice.objects.all().delete()
        return Response("Success", status=status.HTTP_200_OK)

class AboutUs(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kw):
        payload = {
            "About Us": "More Time to you"
        }
        return JsonResponse(payload, status=status.HTTP_200_OK)


class Faq(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kw):
        payload = {
            "What is this": "Fab FResh it is",
            "Another question": "New Ans"
        }
        return Response(payload, status=status.HTTP_200_OK)


class ColorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

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

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

        if isinstance(data, list):
            kwargs["many"] = True

        return super(ClothViewSet, self).get_serializer(*args, **kwargs)

class ClothInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ClothInfo.objects.all()
    serializer_class = ClothInforamtionSerializer

class DriverDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = DriverDetails.objects.all()
    serializer_class = DriverDetailsSerializer

