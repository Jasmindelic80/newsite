from .base import *

import os
import dj_database_url


DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["*"]


# Database (Render daje DATABASE_URL)
DATABASES = {
    "default": dj_database_url.config(default=os.getenv("DATABASE_URL"))
}


# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# WhiteNoise middleware (mora odmah poslije SecurityMiddleware)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
] + MIDDLEWARE


# Django 5/6 način za static storage
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"


try:
    from .local import *
except ImportError:
    pass
