from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth.models import User
from order.models import orders

class UserSerializer(serializers.ModelSerializer):
    UserInfo = serializers.PrimaryKeyRelatedField(many=True, queryset=UserInfo.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=orders.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'UserInfo', 'first_name','orders')


class UserInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = UserInfo

