import os
import socket
from logging import getLogger
from pathlib import Path

from dotenv import load_dotenv
from rest_framework import status


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "True" if str(os.environ.get("DEBUG")).lower() == "true" else "False"

AUTHENTICATION_SERVICE_DOMAIN = os.environ.get("AUTHENTICATION_SERVICE_DOMAIN")

GRPC_PORT = os.environ.get("GRPC_PORT")

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
RABBITMQ_USER = os.environ.get("RABBITMQ_USER")
RABBITMQ_PASS = os.environ.get("RABBITMQ_PASS")
RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT")

ALLOWED_HOSTS: list = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "debug_toolbar",
    "tasks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASS"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "TaskSync API",
    "DESCRIPTION": "API for task tracker",
    "VERSION": "1.0.0",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": "{levelname} {asctime} {pathname} | {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "log.log",
            "formatter": "basic",
        },
    },
    "loggers": {
        "tasks": {
            "handlers": ["file"],
            "level": "WARNING",
        },
    },
}

logger = getLogger("tasks")

grpc_to_http_errors = {
    "OK": status.HTTP_200_OK,
    "CANCELLED": status.HTTP_400_BAD_REQUEST,
    "UNKNOWN": status.HTTP_500_INTERNAL_SERVER_ERROR,
    "INVALID_ARGUMENT": status.HTTP_400_BAD_REQUEST,
    "DEADLINE_EXCEEDED": status.HTTP_504_GATEWAY_TIMEOUT,
    "NOT_FOUND": status.HTTP_404_NOT_FOUND,
    "ALREADY_EXISTS": status.HTTP_409_CONFLICT,
    "PERMISSION_DENIED": status.HTTP_403_FORBIDDEN,
    "RESOURCE_EXHAUSTED": status.HTTP_429_TOO_MANY_REQUESTS,
    "FAILED_PRECONDITION": status.HTTP_400_BAD_REQUEST,
    "ABORTED": status.HTTP_409_CONFLICT,
    "OUT_OF_RANGE": status.HTTP_400_BAD_REQUEST,
    "UNIMPLEMENTED": status.HTTP_501_NOT_IMPLEMENTED,
    "INTERNAL": status.HTTP_500_INTERNAL_SERVER_ERROR,
    "UNAVAILABLE": status.HTTP_503_SERVICE_UNAVAILABLE,
    "DATA_LOSS": status.HTTP_500_INTERNAL_SERVER_ERROR,
    "UNAUTHENTICATED": status.HTTP_401_UNAUTHORIZED,
}

CELERY_BROKER_URL = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
