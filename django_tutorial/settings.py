"""
Django settings for django_tutorial project.
"""

from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent


# ================= SECURITY =================
SECRET_KEY = 'django-insecure-uisrpk$5($3d%7nu(mfxi=(0ly19$*7hg^b70v9k9jnqn2wv3@'
DEBUG = True
ALLOWED_HOSTS = []


# ================= APPLICATIONS =================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'home',

    # Third-party
    'widget_tweaks',
]


# ================= MIDDLEWARE =================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ================= URLS =================
ROOT_URLCONF = 'django_tutorial.urls'


# ================= TEMPLATES =================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # global templates
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


# ================= WSGI =================
WSGI_APPLICATION = 'django_tutorial.wsgi.application'


# ================= DATABASE =================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ================= PASSWORD VALIDATION =================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ================= INTERNATIONALIZATION =================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ================= STATIC FILES (IMPORTANT) =================
STATIC_URL = '/static/'

# Development static folders
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# Production only (keep commented while developing)
# STATIC_ROOT = BASE_DIR / 'staticfiles'


# ================= MEDIA FILES =================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'


# ================= DEFAULT PK =================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ================= CRISPY / WIDGET =================
CRISPY_TEMPLATE_PACK = 'bootstrap4'
