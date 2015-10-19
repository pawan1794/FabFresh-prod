from rest_framework import serializers
from .models import orders

class ordersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = orders
        fields = ('id','amount','status','created_at_time','owner','weight','quantity','order_type')

