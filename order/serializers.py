from rest_framework import serializers
from .models import orders, Size,Type, Color,ClothInfo

class ordersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = orders
        fields = ('id','amount','status','created_at_time','owner','weight','quantity','order_type','p_id' , 'special_instructions')

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

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(ClothInfoSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = ClothInfo


class ClothInforamtionSerializer(serializers.ModelSerializer):
    order = ordersSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    size = SizeSerializer(read_only=True)
    class Meta:

        model = ClothInfo


class ClothsOrdersSerializer(serializers.ModelSerializer):
    clothinformation = ClothInforamtionSerializer(many=True,)
    class Meta:
        model = orders
