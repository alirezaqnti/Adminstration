
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
import os
import sys

SECRET_KEY = str(os.getenv("SECRET_KEY"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


try:
    from .Private import DEBUG
except:
    DEBUG = True

sys.modules['fontawesome_free'] = __import__('fontawesome-free')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "rest_framework.authtoken",
    # "django_filters",
    'fontawesome_free',
    "ckeditor",
    "ckeditor_uploader",
    "debug_toolbar",
    "mptt",
    'Main',
    'Admins',
    'Tasks',
    'Tickets',
    'Messaging',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Main.context_processors.Con',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'

LOGOUT_REDIRECT_URL = '/login/'

if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1','172.20.10.7']
    REFFERER = 'http://127.0.0.1:8000/'
    try:
        from .Private import DATABASES
    except:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

    try:
        from .Private import CACHES
    except:
        # region CACHES
        CACHES = {
                "default": {
                    "BACKEND": "django_redis.cache.RedisCache",
                    "LOCATION": "redis://127.0.0.1:6379",
                }
            }

        # endregion

    # region STATIC

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    STATIC_URL = "/static/"  

    # endregion 
    
    # region MEDIA

    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    # endregion 


# region CAPTCHA

CAPTCHA_FONT_SIZE = 36
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_IMAGE_SIZE = (250,90)
CAPTCHA_LENGTH = 6

# endregion


# region CKEDITOR

CKEDITOR_STORAGE_BACKEND = 'django.core.files.storage.FileSystemStorage'
CKEDITOR_ALLOW_NONIMAGE_FILES = False
X_FRAME_OPTIONS = 'SAMEORIGIN'
CKEDITOR_BASEPATH = f"/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = f"uploads/"
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "toolbar_Custom": [
            [
                "Styles",
                "Format",
                "Bold",
                "Italic",
                "Underline",
                "Strike",
                "SpellChecker",
                "Undo",
                "Redo",
            ],
            ["Link", "Unlink", "Anchor"],
            ["Image", "Flash", "Table", "HorizontalRule"],
            ["TextColor", "BGColor"],
            ["Smiley", "SpecialChar"],
            ["Source"],
            ["Bold", "Italic", "Underline"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
        'height': '500px',
        'width': '100%',
        "filebrowserUploadUrl": "https://salamatid.com/ckeditor/upload/",
    },
}

# endregion


# region EMAIL

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp-ir-01.runflare.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "info@salamatid.com"
EMAIL_HOST_PASSWORD = "Salamatid1402"

# endregion


# region SESSION

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 10000000
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_CACHE_ALIAS = "default"

# endregion


# region Cors

REFERRER_POLICY = 'origin-when-cross-origin'

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# CSRF_COOKIE_SAMESITE = "Lax"

# CSRF_COOKIE_HTTPONLY = True

CORS_EXPOSE_HEADERS = ["Content-Type", "X-CSRFToken"]
CORS_ALLOW_CREDENTIALS = True

# endregion 



INTERNAL_IPS = [
    "127.0.0.1",
]

# region REST_FRAMEWORK

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication"
    ],
}

# endregion

