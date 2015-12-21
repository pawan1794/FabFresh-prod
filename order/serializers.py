from rest_framework import serializers
from .models import orders, Size,Type, Color,ClothInfo,DriverDetails

class ClothInforamtionSerializer(serializers.ModelSerializer):
    '''
    order = ordersSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    class Meta:
        model = ClothInfo
    '''
    color = serializers.ReadOnlyField(source='color.color_name')
    type = serializers.ReadOnlyField(source='type.type_name')
    size = serializers.ReadOnlyField(source='size.size_name')
    class Meta:
        model = ClothInfo
        fields = ('color' , 'type' , 'size' , 'gender')


class ordersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    ClothInfo = ClothInforamtionSerializer(many=True)
    class Meta:
        model = orders
        fields = ('id','amount','status','created_at_time','owner','weight','quantity','order_type','p_id' , 'special_instructions','ClothInfo')

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


class ClothInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothInfo
        many = True



class ClothsOrdersSerializer(serializers.ModelSerializer):
    clothinformation = ClothInforamtionSerializer(read_only=True,many=True,)

    class Meta:
        model = orders