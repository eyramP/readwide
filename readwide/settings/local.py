from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="cswBax7wXrv8sv33RdV9ZiUpXnv77CoxInQNp5vas1tz9Cuu7Ts",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
