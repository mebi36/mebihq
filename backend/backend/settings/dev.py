from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@jyt$g=b*8$dypay&zbpff#y*vrum9fv=#xyyuwybd*9grggk^"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["mebihq.herokuapp.com", "localhost", "35.172.194.18"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
