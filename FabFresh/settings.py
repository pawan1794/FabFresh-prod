import os
import urllib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '+m*(+1@a!$cu(1*rn5o56bu%*$*%h(n$oai#grpbv+#b9w=&kc'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'rest_framework',
    'oauth2_provider',
    'corsheaders',
    'users',
    'order',
    'rest_framework_swagger',
    'push_notifications',

    #celery
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = 'FabFresh.urls'
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    )
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FabFresh.wsgi.application'

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fabfreshtest',
            'USER': 'hari',
            'PASSWORD': 'hari',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PUSH_NOTIFICATIONS_SETTINGS = {
        "GCM_API_KEY": "AIzaSyC7r-bihlBSfZ3MfHfMCmbshjOloiUCFBU",
        "APNS_CERTIFICATE" : "/home/hari/Downloads/apns-dev-cert.pem"
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..','static') 
#STATIC_ROOT = "/opt/python/current/app/FabFresh/FabFresh/static"


SOCIAL_AUTH_ENABLED_BACKENDS=('facebook')

SOCIAL_AUTH_FACEBOOK_KEY = '1640925132856151'
SOCIAL_AUTH_FACEBOOK_SECRET = '5fc388d8613577ec2b1ce2d74b19c424'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@fabfresh.in'
EMAIL_HOST_PASSWORD = 'fabfresh123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


'''
CELERY_IMPORTS=('order.tasks')
CELERY_RESULT_BACKEND = 'amqp'
CELERY_TASK_RESULT_EXPIRES = 18000


#SQS
AWS_ACCESS_KEY = 'AKIAIWH34GQPAG7KQLRA'
AWS_SECRET_KEY = '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'
'''


'''
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'yaml']
CELERY_RESULT_SERIALIZER = 'json'

CELERY_ENABLE_REMOTE_CONTROL = False
CELERY_SEND_EVENTS = False

CELERY_ENABLE_UTC = True
CELERY_DISABLE_RATE_LIMITS = True

#BROKER_TRANSPORT = 'sqs'
BROKER_URL = 'https://sqs.eu-west-1.amazonaws.com/649666883728/fabfresh@'.format(AWS_ACCESS_KEY, urllib.quote(AWS_SECRET_KEY, safe=''))
BROKER_TRANSPORT_OPTIONS = {
 'queue_name_prefix': 'fabfresh',
 'visibility_timeout': 60, # seconds
 'wait_time_seconds': 20,  # Long polling
 'region' : 'eu-west-1'
}

BROKER_URL = 'sqs://'+ AWS_ACCESS_KEY + ':' + AWS_SECRET_KEY + 'fabfresh@:80//'
BROKER_TRANSPORT_OPTIONS = {
    'region' : 'eu-west-1',
    'sdb_persistence': False
}
'''