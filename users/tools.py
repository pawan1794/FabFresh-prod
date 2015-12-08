from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from django.http import JsonResponse
from oauth2_provider.models import AccessToken, Application, RefreshToken
from django.utils.timezone import now, timedelta
import requests
from django.core.mail import send_mail
from django.conf import settings
from models import User,UserInfo

#Method to be called for sending message
def message(phone ,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+phone+"&text="+message+"&priority=ndnd&stype=normal"
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
            print "inside phone1"
            u = User.objects.get(id = user.id)
            print "inside phone2"
            print u.id
            up = UserInfo.objects.get(owner = u.id)
            print u
            if not up.phone:
                print "inside phone3"
                userInfo = UserInfo.objects.filter(owner = u)
                userInfo.update(phone=number)
                print "inside phone4"
                print "inside phon5"
        #sending message to new registered users
        text_message = "Dear "+ str(user) +" , Thanks for Signing up with FabFresh . More Time to You ! from now on . "
        message(number,text_message)
        #send email
        send_mail('FabFresh Welcome\'s You', 'Welcome to FabFresh. We are happy to have you. More Time to You ! from now on', settings.EMAIL_HOST_USER, [str(email)], fail_silently=False)
    return JsonResponse(token)


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