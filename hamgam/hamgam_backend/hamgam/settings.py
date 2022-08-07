"""
Django settings for hamgam project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
y

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os 
import socket

from dotenv import load_dotenv
BASE_URL = 'https://hamgam-srbiau.ir'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY ='lacaa612c*sac56a1212^#&2de2d4w86'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#<<<<<<< HEAD
ALLOWED_HOSTS = ['ham-ghadam.ir', 'www.ham-ghadam.ir']
#=======
#ALLOWED_HOSTS = ['0.0.0.0']
#>>>>>>> 65426fe87fbeacbf765924ede6849e747392e57c


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External 
    "debug_toolbar",
    'rest_framework',
    'rest_framework.authtoken',
    'authemail',
    'ckeditor_uploader',
    'ckeditor', 
    # CORS
    'corsheaders',
    'django_extensions',
    
    
    # Internal 
    'account.apps.AccountConfig',
    'idea.apps.IdeaConfig',
    'skill.apps.SkillConfig',
    'docs.apps.DocsConfig',
]   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    "django.middleware.csrf.CsrfViewMiddleware",    # Debug toolbar  
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # LEAKED PASSWORDS 
    'pwned_passwords_django.middleware.PwnedPasswordsMiddleware',
    # CORS
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
]



INTERNAL_IPS = [
    "127.0.0.1",
    
]

ROOT_URLCONF = 'hamgam.urls'

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

WSGI_APPLICATION = 'hamgam.wsgi.application'

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.postgresql',
#       'NAME': os.environ.get('POSTGRESQL_DB_NAME'),
#       'USER': os.environ.get('POSTGRESQL_DB_USER'),
#       'PASSWORD': os.environ.get('POSTGRESQL_DB_PASSWORD'),
#       'HOST': os.environ.get('POSTGRESQL_DB_HOST'),
#       'PORT': os.environ.get('POSTGRESQL_DB_PORT'),
#   }
#}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
STATIC_URL = '/static/'

STATIC_ROOT = '/home/mehdi/source/stat/static'
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
    {
        'NAME':'pwned_passwords_django.validators.PwnedPasswordsValidator',
        'OPTIONS': {'error_message': ('این رمز عبور قبلا هک شده بوده. برای اطلاعات بیشتر /n https://haveibeenpwned.com/ /n  یک سری بزنید')}
    }
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_FROM_EMAIL = 'info@ham-ghadam.ir'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# URL 
ALLOW_UNICODE_SLUGS = True

#### EMIAL STUFF
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

#EMAIL_FROM = os.environ.get('AUTHEMAIL_DEFAULT_EMAIL_FROM') or '<YOUR DEFAULT_EMAIL_FROM HERE>'
#EMAIL_BCC = os.environ.get('AUTHEMAIL_DEFAULT_EMAIL_BCC') or '<YOUR DEFAULT_EMAIL_BCC HERE>'

#EMAIL_HOST = 'localhost'   
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'info'
#EMAIL_HOST_PASSWORD = ''


STATIC_URL = '/static/'


 # Cors 

#CORS_ORIGIN_ALLOW_ALL = True
#<<<<<<< HEAD
CORS_ALLOWED_ORIGINS = [
    #"https://example.com",
    #"https://sub.example.com",\
    "http://localhost:8080",
#    "http://localhost",
#    "http://144.76.186.13",
#    "http://localhost:80",
#    "http://144.76.186.13:80",
    #"144.76.186.13"
    #"http://127.0.0.1:9000",
]


#CSRF_TRUSTED_ORIGINS = [
 #   "http:/localhost:80",
#]

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
#=======
#CSRF_TRUSTED_ORIGINS = ['localhost']
#>>>>>>> 65426fe87fbeacbf765924ede6849e747392e57c
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Account Models
AUTH_USER_MODEL = 'account.Account'


# Logging 
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/../../hamgam/logs/debug.log',
        }

    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
'''
## Coolkie Sessions 



REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
	)
}
# Email 

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_email')



# Media 
BASE_MEDIA_DIR = '/home/mehdi/source/images'
MEDIA_URL = "/media/"
# any file field upload by default
MEDIA_ROOT =  f"{BASE_MEDIA_DIR}/media"

PROTECTED_MEDIA =  f"{BASE_MEDIA_DIR}/protected"


# Caching Using Redis 
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#        #'LOCATION': 'redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@127.0.0.1:6379',
#        'LOCATION': 'redis://127.0.0.1:6379',
#        'OPTIONS': {
#        'db': '0',
#        'parser_class': 'redis.connection.PythonParser',
#        'pool_class': 'redis.BlockingConnectionPool', 
#        }
#    },
#}


CKEDITOR_BASEPATH = "/home/mehdi/source/stat/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        #'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 600,
        'width': 1000, 
        'tabSpaces': 4,
        #'skin': 'monoo color',
        # Toolbar Style
        # Add Code Block Plug-ins
        'extraPlugins': ','.join(['codesnippet',]),
    },
}
CKEDITOR_IMAGE_BACKEND = 'pillow' 