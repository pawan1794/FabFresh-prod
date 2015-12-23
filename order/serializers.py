from rest_framework import serializers
from .models import orders, Size,Type, Color,ClothInfo,DriverDetails,Brand, StatusTimeStamp

class ClothInforamtionSerializer(serializers.ModelSerializer):
    color = serializers.ReadOnlyField(source='color.color_name')
    type = serializers.ReadOnlyField(source='type.type_name')
    size = serializers.ReadOnlyField(source='size.size_name')
    brand = serializers.ReadOnlyField(source='brand.brand_name')
    class Meta:
        model = ClothInfo
        fields = ('color' , 'type' , 'size' , 'brand' , 'gender')


class ordersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    ClothInfo = ClothInforamtionSerializer(many=True)
    class Meta:
        model = orders
        fields = ('id','amount','status','created_at_time','modified_at_time','owner','weight','quantity','order_type','p_id' , 'special_instructions','ClothInfo')

class StatusTimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTimeStamp


class DriverDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDetails


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color

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