from .base import *


INSTALLED_APPS += ['zappa_django_utils']

DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'sqlite.db',
        'BUCKET': 'pythonist-db'
    }
}

S3_BUCKET = "pythonist1"
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET
STATIC_URL = f"https://{S3_BUCKET}.s3.amazonaws.com/"
