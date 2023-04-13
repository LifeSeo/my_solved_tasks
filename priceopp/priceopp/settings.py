from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '123456'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'main',
    'news',
    'reviews',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'captcha',
    'django.contrib.postgres',
    'bootstrap3',
    'sendemail',
    'ckeditor_uploader',
    'django_ckeditor_5',
    'rating.apps.RatingConfig',
    'easy_thumbnails',
    'newsletter',
    'django_crontab',
    "django_cron",
    'rest_framework',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'priceopp.urls'

NEWSLETTER_THUMBNAIL = 'easy-thumbnails'
NEWSLETTER_CONFIRM_EMAIL = False
SITE_ID = 1

# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1

# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60

# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100

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

WSGI_APPLICATION = 'priceopp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "supp0rt.priceopp@yandex.ru"
EMAIL_HOST_PASSWORD = "Buben2424%"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

RECIPIENTS_EMAIL = ['supp0rt.priceopp@yandex.ru']
DEFAULT_FROM_EMAIL = 'supp0rt.priceopp@yandex.ru'

LOGIN_REDIRECT_URL = 'home'

RECAPTCHA_PUBLIC_KEY = '6LcDzzElAAAAALUNHsPbkBRuAadOVbvaD1lePLbI'
RECAPTCHA_PRIVATE_KEY = '6LcDzzElAAAAALwjVgYwUwtjkxG_7N34xT3qyaXq'

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_IMAGE_SIZE = (187, 41)
CAPTCHA_FONT_SIZE = (24)
CAPTCHA_BACKGROUND_COLOR = '#cccccc'
CAPTCHA_FOREGROUND_COLOR = '#001100'
CAPTCHA_LENGTH = 8

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/assets/ckeditor/ckeditor/"
CKEDITOR_5_CUSTOM_CSS = '/main/css/main.css'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote', 'imageUpload'
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],

        'image': {
            'toolbar': ['imageTextAlternative', 'imageTitle', '|', 'imageStyle:alignLeft', 'imageStyle:full',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',]
            },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ],
            'height': 500,
        'width': '100%',
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True
        }
    }
}