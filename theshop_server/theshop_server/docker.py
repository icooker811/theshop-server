from .settings import *
env = os.environ.get

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't+1v*0e%uz4u4*=v-s40&y$rrtt7s%rl^r)2j^-h_x(l7(bjxb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']

from mongoengine import connect, connection
connection.disconnect()
connect('theshop-db', host='mongo')

CACHES['default']['LOCATION'] = 'redis://redis:6379/1'

# CELERY SETTINGS
BROKER_URL = 'redis://redis:6379/0'
GOOGLE_API_KEY = env('GOOGLE_API_KEY') or ''
FCM_API_KEY = env('FCM_API_KEY') or ''

FCM_DJANGO_SETTINGS = {
       "FCM_SERVER_KEY": FCM_API_KEY,
       "ONE_DEVICE_PER_USER": True,
       "DELETE_INACTIVE_DEVICES": True,
}
