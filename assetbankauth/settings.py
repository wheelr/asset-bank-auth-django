import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'ONLY-USED-FOR-TESTING'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ASSETBANK_AUTH_ENABLED = True
ASSETBANK_AUTH_TOKEN_KEY = ''
ASSETBANK_URL = 'http://localhost:8080/asset-bank'
ASSETBANK_LOG_OUT_AFTER_AUTH = False
