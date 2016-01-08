from rest_framework import serializers
from .models import orders, Size,Type, Color,ClothInfo,DriverDetails,Brand, StatusTimeStamp, Coupon

from django.contrib.auth.models import User
from users.models import UserProfile

class ClothInforamtionSerializer(serializers.ModelSerializer):
    color = serializers.ReadOnlyField(source='color.color_name')
    type = serializers.ReadOnlyField(source='type.type_name')
    size = serializers.ReadOnlyField(source='size.size_name')
    brand = serializers.ReadOnlyField(source='brand.brand_name')
    class Meta:
        model = ClothInfo
        fields = ('color' , 'type' , 'size' , 'brand' , 'gender')

class StatusTimeStampSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusTimeStamp
        fields = ('status' , 'timestamp')

class DriverDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDetails


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon

class ordersSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    ClothInfo = ClothInforamtionSerializer(many=True)
    StatusTimeStamp = StatusTimeStampSerializer(many=True)
    DriverDetails = DriverDetailsSerializer(many=True)
    coupon = serializers.ReadOnlyField(source='coupon.coupon_tag')

    class Meta:
        model = orders
        fields = ('id','amount','status','created_at_time','modified_at_time','owner','weight','quantity','order_type',
                  'p_id', 'special_instructions','ClothInfo','StatusTimeStamp','DriverDetails','coupon')



class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color

from users.serializers import PhoneNumberSerializer

class CustomerDetailSerializer(serializers.ModelSerializer):
    #customer_details
    name = serializers.ReadOnlyField(source='owner.username')
    address_line_1 = serializers.ReadOnlyField(source='address')
    address_line_2 = serializers.ReadOnlyField(source='addressSubLocality')
    latitude = serializers.ReadOnlyField(source='addressLatitude')
    longitude = serializers.ReadOnlyField(source='addressLogitude')
    city = serializers.SerializerMethodField('get_city_name')


    class Meta:
        model = UserProfile
        fields = ('name', 'address_line_1','address_line_2','city','latitude','longitude')

    def get_city_name(self,obj):
        return 'Bangalore'


#order_details
class ShadowfaxSerializer(serializers.ModelSerializer):

    client_order_id = serializers.ReadOnlyField(source='id')
    order_value = serializers.ReadOnlyField(source='amount')
    paid = serializers.SerializerMethodField('get_payment_status')

    class Meta:
        model = orders
        fields = ('client_order_id','order_value','paid')

    def get_payment_status(self,obj):
        return 'true'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand

class ClothInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothInfo
        many = True



class ClothsOrdersSerializer(serializers.ModelSerializer):
    clothinformation = ClothInforamtionSerializer(read_only=True,many=True,)

    class Meta:
        model = orders

'''from users.serializers import *
class UserSerializer(serializers.ModelSerializer):
    UserInfo = PhoneNumberSerializer()
    UserProfile = UserProfileSerializer(many=True)
    Wallet = WalletSerializer(read_only=True)
    #UserInfo = serializers.PrimaryKeyRelatedField(queryset=UserInfo.objects.all())
    queryset = orders.objects.get(id=21)
    orders = ShadowfaxSerializer(queryset,many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'UserInfo','UserProfile', 'first_name','orders','email','Wallet')
'''