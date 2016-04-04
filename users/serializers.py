from rest_framework import serializers
from .models import UserInfo, UserProfile,PostalCode, Wallet, AndroidAppVersion, NotificationBoard, AllInOne #, Locality, Address, City
from django.contrib.auth.models import User
from order.models import orders
from oauth2_provider.models import AccessToken, RefreshToken
from django.utils import timezone

class AllInOneSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = AllInOne

class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode

class UserInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = UserInfo

class WalletSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Wallet

#Only to get phone number[userinfo model]
class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('phone','flag')

#Getting address
class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserProfile

class UserSerializer(serializers.ModelSerializer):
    UserInfo = PhoneNumberSerializer()
    UserProfile = UserProfileSerializer(many=True)
    Wallet = WalletSerializer(read_only=True)
    #UserInfo = serializers.PrimaryKeyRelatedField(queryset=UserInfo.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=orders.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'UserInfo','UserProfile', 'first_name','orders','email','Wallet')

#new change
class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password','email')
        write_only_fields = ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()


class ChangePasswordSerializer(ResetPasswordSerializer):
    password = serializers.CharField()

class AndroidAppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidAppVersion

class NotificationBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationBoard