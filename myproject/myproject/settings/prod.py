from myproject.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = open(secretfile)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['myhost.com']
try:
    from myproject.settings.local import *
except ImportError:
    pass