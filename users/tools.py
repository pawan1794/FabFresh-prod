from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from django.http import JsonResponse
from oauth2_provider.models import AccessToken, Application, RefreshToken
from django.utils.timezone import now, timedelta
import requests

def message(phone ,message):
    url1 = "http://bhashsms.com/api/sendmsg.php?user=7204680605&pass=9ba84c5&sender=Ffresh&phone="+phone+"&text="+message+"&priority=ndnd&stype=normal"
    r1 = requests.get(url1)

def get_token_json(access_token, a, number,user):
    token = {
        'access_token': access_token.token,
        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'token_type': 'Bearer',
        'refresh_token': access_token.refresh_token.token,
        'scope': access_token.scope,
        'user_status' : a
    }
    if a == 1:
        text_message = "Dear "+ str(user) +" , Thanks for Signing up with FabFresh . More Time to You ! from now on . "
        message(number,text_message)

    return JsonResponse(token)


def get_access_token(user,number):
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
    #oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS = 10000000000000
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

    return get_token_json(access_token,a,number,user)