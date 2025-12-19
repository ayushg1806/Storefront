from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-cxr7vdzbenz^$2a7amfd42ghl$kpjiz_xib!tf6e-&ss1^umh#'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Ayush@1806',
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8001',
    'http://127.0.0.1:8001',
]