from rest_framework import serializers
from .models import UserInfo, UserProfile #, Locality, Address, City
from django.contrib.auth.models import User
from order.models import orders

class UserInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = UserInfo

#Only to get phone number[userinfo model]
class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('phone',)

#Getting address
class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserProfile

class UserSerializer(serializers.ModelSerializer):
    UserInfo = PhoneNumberSerializer()
    UserProfile = UserProfileSerializer(many=True)
    #UserInfo = serializers.PrimaryKeyRelatedField(queryset=UserInfo.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=orders.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'UserInfo','UserProfile', 'first_name','orders','email')

'''
class UserInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserInfo

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    #address = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name = 'address-detail')

    class Meta:
        model = UserProfile
'''


