from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from django.http import JsonResponse
from oauth2_provider.models import AccessToken, Application, RefreshToken
from django.utils.timezone import now, timedelta
import requests
from django.core.mail import send_mail
from django.conf import settings
from models import User,UserInfo
import logging
import random

logger = logging.getLogger(__name__)

#Method to be called for sending message
def message(phone ,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+str(phone)+"&text="+message+"&priority=ndnd&stype=normal"
    r1 = requests.get(url1)

def get_token_json(access_token, a, number,user,email):
    #Creates json format of Access Token withe refereshtoken
    token = {
        'access_token': access_token.token,
        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'token_type': 'Bearer',
        'refresh_token': access_token.refresh_token.token,
        'scope': access_token.scope,
        'user_status' : a,
        'phone' : number
    }
    if a == 1:
        if number:
            u = User.objects.get(id = user.id)
            up = UserInfo.objects.get(owner = u.id)
            userInfo = UserInfo.objects.filter(owner = u)
            if not up.phone:
                userInfo.update(phone=number)
        #sending message to new registered users
        text_message = "Dear "+ str(user) +" , Thanks for Signing up with FabFresh . More Time to You ! from now on . "
        message(number,text_message)

        #OTP
        otp = random.randint(10000,1000000)
        OTP_text_message = "OTP:"+ str(otp) + ". Use the above OTP to verify you mobile number on FabFresh"
        message(number,OTP_text_message)
        userInfo.update(otp=otp)

        #send email
        send_mail('FabFresh Welcome\'s You', 'Welcome to FabFresh. We are happy to have you. More Time to You ! from now on', settings.EMAIL_HOST_USER, [str(email)], fail_silently=False)
        logger.info("New User " + str(user) + " has registered with fabfresh" )
        return JsonResponse(token)
    else:
        if number:
            u = User.objects.get(id = user.id)
            up = UserInfo.objects.get(owner = u.id)
            if up.phone is not int(number):
                up.phone = number
                data  = "Phone number already registered"
                print UserInfo.objects.filter(phone = number,flag = True).count()
                if UserInfo.objects.filter(phone = number,flag = True).count() :
                    return JsonResponse({'status':data})

                otp = random.randint(10000,1000000)
                OTP_text_message = "OTP:"+ str(otp) + ". Use the above OTP to verify you mobile number on FabFresh"
                message(number,OTP_text_message)
                up.otp = otp
                up.flag = False
                up.save()

        token1 = {
        'access_token': access_token.token,
        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'token_type': 'Bearer',
        'refresh_token': access_token.refresh_token.token,
        'scope': access_token.scope,
        'user_status' : a,
        }
        logger.info("New Access token " + access_token.token + " is assigined for user " + str(user))
        return JsonResponse(token1)


def get_access_token(user,number,email):
    app = Application.objects.get(name="FabFresh")
    a = 1
    try:
        old_access_token = AccessToken.objects.get(
            user=user, application=app)
        old_refresh_token = RefreshToken.objects.get(
            user=user, access_token=old_access_token
        )
    except:
        pass
    else:
        #set 0 if exsisting user
        a = 0
        logger.info("Deleting Old Access Token for " + str(user) + " " + str(old_access_token))
        old_access_token.delete()
        old_refresh_token.delete()

    token = generate_token()
    refresh_token = generate_token()
    oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS = 100000000
    expires = now() + timedelta(seconds=oauth2_settings.
                                ACCESS_TOKEN_EXPIRE_SECONDS)
    scope = "read write"


    access_token = AccessToken.objects.\
        create(user=user,
               application=app,
               expires=expires,
               token=token,
               scope=scope)

    RefreshToken.objects.\
        create(user=user,
               application=app,
               token=refresh_token,
               access_token=access_token)
    return get_token_json(access_token,a,number,user,email)