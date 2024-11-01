"""
Django settings for meshdb project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import logging
import os
from pathlib import Path
from typing import Any, Dict, List

from django.http.request import HttpRequest
from dotenv import load_dotenv

load_dotenv()

MESHDB_ENVIRONMENT = os.environ.get("MESHDB_ENVIRONMENT", "")

if not MESHDB_ENVIRONMENT:
    logging.warning("Please specify MESHDB_ENVIRONMENT environment variable. Things will not work properly without it.")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Log users out automatically after 2 days
SESSION_COOKIE_AGE = 172800  # Expire sessions after 2 Days. "1209600(2 weeks)" by default
SESSION_SAVE_EVERY_REQUEST = True  # "False" by default

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False") == "True"
PROFILING_ENABLED = DEBUG and not os.environ.get("DISABLE_PROFILING", "False") == "True"


FLAGS: Dict[str, Any] = {
    "MAINTENANCE_MODE": [],
    "EDIT_PANORAMAS": [],
    "INTEGRATION_ENABLED_SEND_JOIN_REQUEST_SLACK_MESSAGES": [],
    "INTEGRATION_ENABLED_CREATE_OSTICKET_TICKETS": [],
}

USE_X_FORWARDED_HOST = True

SECURE_HSTS_SECONDS = 30  # TODO: Increase me to 31536000 https://github.com/nycmeshnet/meshdb/issues/642
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

CSP_REPORT_ONLY = True  # TODO: Set me to false https://github.com/nycmeshnet/meshdb/issues/644
CSP_DEFAULT_SRC = [
    "'self'",
    "https://*.nycmesh.net",
    "https://maps.googleapis.com",
    "https://maps.gstatic.com",
    "https://fonts.googleapis.com",
    "https://fonts.gstatic.com",
    "https://cdn.jsdelivr.net",
    "data:",
    "https://cdn.redoc.ly",  # Redoc
    "blob:",  # Redoc
    "'unsafe-inline'",  # TODO: Remove me https://github.com/nycmeshnet/meshdb/issues/645
    "*.browser-intake-us5-datadoghq.com",
]
CSP_IMG_SRC = [
    "'self'",
    "https://maps.googleapis.com",
    "https://maps.gstatic.com",
    "https://cdn.jsdelivr.net",
    "https://cdn.redoc.ly",  # Redoc
    "https://node-db.netlify.app",  # Panorama images
]
CSP_REPORT_URI = [
    "https://csp-report.browser-intake-us5-datadoghq.com/api/v2/logs"
    "?dd-api-key=pubca00a94e49167539d2e291bea2b0f20f&dd-evp-origin=content-security-policy"
    f"&ddsource=csp-report&ddtags=service%3Ameshdb%2Cenv%3A{MESHDB_ENVIRONMENT}"
]

# We don't use any of these advanced features, so be safe and disallow any scripts from
# using them on our pages
PERMISSIONS_POLICY: Dict[str, List[str]] = {
    "accelerometer": [],
    "ambient-light-sensor": [],
    "autoplay": [],
    "camera": [],
    "display-capture": [],
    "document-domain": [],
    "encrypted-media": [],
    "fullscreen": [],
    "geolocation": [],
    "gyroscope": [],
    "interest-cohort": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "usb": [],
}

LOS_URL = os.environ.get("LOS_URL", "https://devlos.mesh.nycmesh.net")
MAP_URL = os.environ.get("MAP_BASE_URL", "https://devmap.mesh.nycmesh.net")
FORMS_URL = os.environ.get("FORMS_URL", "https://devforms.mesh.nycmesh.net")

# SMTP Config for password reset emails
EMAIL_HOST = os.environ.get("SMTP_HOST")
EMAIL_PORT = os.environ.get("SMTP_PORT")
EMAIL_HOST_USER = os.environ.get("SMTP_USER")
EMAIL_HOST_PASSWORD = os.environ.get("SMTP_PASSWORD")
EMAIL_USE_TLS = True

ALLOWED_HOSTS = [
    "db.mesh.nycmesh.net",
    "db.mesh",
    "db.nycmesh.net",
    "meshdb",
    "nginx",
    "devdb.mesh.nycmesh.net",
    "devdb.nycmesh.net",
]

CORS_ALLOWED_ORIGINS = [
    "https://forms.mesh.nycmesh.net",
    "https://devforms.mesh.nycmesh.net",
    "https://forms.nycmesh.net",
    "https://forms.devdb.nycmesh.net",
    "https://map.mesh.nycmesh.net",
    "https://devmap.mesh.nycmesh.net",
    "https://map.db.nycmesh.net",
    "https://map.devdb.nycmesh.net",
    "https://adminmap.mesh.nycmesh.net",
    "https://devadminmap.mesh.nycmesh.net",
    "https://adminmap.db.nycmesh.net",
    "https://adminmap.devdb.nycmesh.net",
    "https://devdb.nycmesh.net",
]

CSRF_TRUSTED_ORIGINS = [
    "http://meshdb:8081",
    "http://nginx:8080",
    "https://db.nycmesh.net",
    "https://devdb.nycmesh.net",
    "http://devdb.mesh.nycmesh.net",
    "https://devdb.mesh.nycmesh.net",
    "http://db.mesh.nycmesh.net",
    "https://db.mesh.nycmesh.net",
]

if DEBUG:
    ALLOWED_HOSTS += [
        "127.0.0.1",
        "host.docker.internal",
    ]

    CORS_ALLOWED_ORIGINS += [
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "http://127.0.0.1:80",
        "http://localhost:80",
    ]

    CSRF_TRUSTED_ORIGINS += [
        "http://127.0.0.1:8080",
        "http://127.0.0.1",
    ]

    CSP_DEFAULT_SRC += [
        "*",
    ]

# Application definition

INSTALLED_APPS = [
    "meshdb.apps.MeshDBAdminConfig",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "drf_hooks",
    "rest_framework",
    "rest_framework.authtoken",
    "meshapi",
    "meshapi_hooks",
    "meshweb",
    "corsheaders",
    "drf_spectacular",
    "django_filters",
    "django_jsonform",
    "dbbackup",
    "import_export",
    "flags",
    "explorer",
    "simple_history",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django_permissions_policy.PermissionsPolicyMiddleware",
    "csp.middleware.CSPMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "meshweb.middleware.MaintenanceModeMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]


if PROFILING_ENABLED:
    INSTALLED_APPS.append("silk")
    MIDDLEWARE.append("silk.middleware.SilkyMiddleware")
    MIDDLEWARE.append("django_cprofile_middleware.middleware.ProfilerMiddleware")

SILKY_IGNORE_PATHS = ["/admin/jsi18n/"]

DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False

ROOT_URLCONF = "meshdb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "meshdb/templates"), os.path.join(BASE_DIR, "meshapi/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "meshdb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", 5432),
    },
    "readonly": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER_RO"),
        "PASSWORD": os.environ.get("DB_PASSWORD_RO"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", 5432),
    },
}

# django-dbbackup
# https://django-dbbackup.readthedocs.io/en/master/installation.html

DBBACKUP_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DBBACKUP_FILENAME_TEMPLATE = "{datetime}.{extension}"
DBBACKUP_STORAGE_OPTIONS = {
    "bucket_name": "meshdb-data-backups",
    "location": "meshdb-backups/prod/",
}

DBBACKUP_CONNECTORS = {
    "default": {
        # "SINGLE_TRANSACTION": False,
        "IF_EXISTS": True
    }
}
DBBACKUP_DATABASES = ["default"]

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

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True

LOGOUT_REDIRECT_URL = "/admin/login/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    # BASE_DIR / "static", # The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting
    "/var/www/static/",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "meshapi.util.drf_utils.CustomSizePageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        # Removes HTML form (doesn't work with NestedKeyObjectRelatedField)
        "meshapi.util.drf_renderer.OnlyRawBrowsableAPIRenderer",
    ],
}

HOOK_EVENTS = {
    "building.created": "meshapi.Building.created+",
    "member.created": "meshapi.Member.created+",
    "install.created": "meshapi.Install.created+",
    "node.created": "meshapi.Node.created+",
    "link.created": "meshapi.Link.created+",
    "los.created": "meshapi.LOS.created+",
    "device.created": "meshapi.Device.created+",
    "sector.created": "meshapi.Sector.created+",
    "access_point.created": "meshapi.AccessPoint.created+",
    "building.updated": "meshapi.Building.updated+",
    "member.updated": "meshapi.Member.updated+",
    "install.updated": "meshapi.Install.updated+",
    "node.updated": "meshapi.Node.updated+",
    "link.updated": "meshapi.Link.updated+",
    "los.updated": "meshapi.LOS.updated+",
    "device.updated": "meshapi.Device.updated+",
    "sector.updated": "meshapi.Sector.updated+",
    "access_point.updated": "meshapi.AccessPoint.updated+",
    "building.deleted": "meshapi.Building.deleted+",
    "member.deleted": "meshapi.Member.deleted+",
    "install.deleted": "meshapi.Install.deleted+",
    "node.deleted": "meshapi.Node.deleted+",
    "link.deleted": "meshapi.Link.deleted+",
    "los.deleted": "meshapi.LOS.deleted+",
    "device.deleted": "meshapi.Device.deleted+",
    "sector.deleted": "meshapi.Sector.deleted+",
    "access_point.deleted": "meshapi.AccessPoint.deleted+",
}

HOOK_SERIALIZERS = {
    "meshapi.Building": "meshapi.serializers.model_api.BuildingSerializer",
    "meshapi.Member": "meshapi.serializers.model_api.MemberSerializer",
    "meshapi.Install": "meshapi.serializers.model_api.InstallSerializer",
    "meshapi.Node": "meshapi.serializers.model_api.NodeSerializer",
    "meshapi.Link": "meshapi.serializers.model_api.LinkSerializer",
    "meshapi.LOS": "meshapi.serializers.model_api.LOSSerializer",
    "meshapi.Device": "meshapi.serializers.model_api.DeviceSerializer",
    "meshapi.Sector": "meshapi.serializers.model_api.SectorSerializer",
    "meshapi.AccessPoint": "meshapi.serializers.model_api.AccessPointSerializer",
}

HOOK_CUSTOM_MODEL = "meshapi_hooks.CelerySerializerHook"

SPECTACULAR_SETTINGS = {
    "TITLE": "MeshDB Data API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "TAGS": [
        {"name": "API Status", "description": "Meta-endpoint to indicate API status"},
        {"name": "Members", "description": "Members of the mesh and their contact details"},
        {"name": "Buildings", "description": "Buildings on the mesh and their location data, one per street address"},
        {
            "name": "Installs",
            "description": "Installs, one corresponding to each household that is either already on the mesh, "
            "or wishes to join the mesh. For convenience this category offers two different methods to access the same "
            "database objects. Either database UUID or install_number can be used interchanably in any of the URLs for "
            "this object",
        },
        {
            "name": "Nodes",
            "description": "Nodes, one corresponding to each collection of devices with the same network number, "
            "the installs that use those devices, and the buildings that house them. For convenience this category "
            "offers two different methods to access the same database objects. Either database UUID or network_number "
            "can be used interchanably in any of the URLs for this object. Note that not all Nodes have a "
            "network_number (that field is only required for active nodes)",
        },
        {"name": "Links", "description": "Network links between devices"},
        {
            "name": "LOSes",
            "description": "Lines of sight between buildings, primarily useful to document potential future links",
        },
        {
            "name": "Devices",
            "description": "Devices, one corresponding to each physical device on the mesh (routers, aps, cpes, etc.). "
            "Includes all Sectors and Access Points",
        },
        {
            "name": "Sectors",
            "description": 'Special devices with antennas with broad coverage of a radial "slice" of land area. '
            "See https://wiki.mesh.nycmesh.net/books/3-hardware-firmware/page/ubiquiti-liteap-sector#bkmrk-page-title",
        },
        {
            "name": "Access Points",
            "description": "Special devices which provide community WiFi to a given area, usually in a park or "
            "other public place",
        },
        {"name": "Geographic & KML Data", "description": "Endpoints for geographic and KML data export"},
        {
            "name": "Website Map Data",
            "description": "Endpoints used to power the nycmesh.net website map. "
            "Uses a legacy data format, not recommended for new applications",
        },
        {
            "name": "Legacy Query Form",
            "description": "Endpoints used to power the legacy docs query form. "
            "Uses a legacy data format, not recommended for new applications",
        },
        {"name": "User Forms", "description": "Forms exposed directly to humans"},
        {
            "name": "Panoramas",
            "description": "Used to bulk ingest panoramas. Internal use only (use Building.panoramas instead)",
        },
    ],
    "SWAGGER_UI_SETTINGS": {
        "defaultModelsExpandDepth": 10,
        "defaultModelExpandDepth": 10,
        "displayRequestDuration": True,
        "docExpansion": "none",
    },
}

IMPORT_EXPORT_IMPORT_PERMISSION_CODE = "add"
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = "view"

SIMPLE_HISTORY_HISTORY_ID_USE_UUID = True

EXPLORER_CONNECTIONS = {"Default": "readonly"}
EXPLORER_DEFAULT_CONNECTION = "readonly"
EXPLORER_NO_PERMISSION_VIEW = "meshweb.views.explorer_auth_redirect"


def EXPLORER_PERMISSION_VIEW(r: HttpRequest) -> bool:
    return r.user.has_perm("meshapi.explorer_access")


def EXPLORER_PERMISSION_CHANGE(r: HttpRequest) -> bool:
    return r.user.has_perm("meshapi.explorer_access")


EXPLORER_ENABLE_ANONYMOUS_STATS = False
EXPLORER_SQL_BLACKLIST = (
    # DML
    "COMMIT",
    "DELETE",
    "INSERT",
    "MERGE",
    "REPLACE",
    "ROLLBACK",
    "SET",
    "START",
    "UPDATE",
    "UPSERT",
    # DDL
    "ALTER",
    "CREATE",
    "DROP",
    "RENAME",
    "TRUNCATE",
    # DCL
    "GRANT",
    "REVOKE",
)


EXPLORER_SCHEMA_EXCLUDE_TABLE_PREFIXES = [
    "authtoken_",
    "django_",
    "auth_",
    "contenttypes_",
    "sessions_",
    "admin_",
    "flags_",
    "explorer_",
    "meshapi_hooks_",
]
