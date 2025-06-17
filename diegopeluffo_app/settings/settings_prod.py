from .settings_base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("La variable de entorno 'SECRET_KEY' no está configurada para producción. Es crucial para la seguridad.")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INSTALLED_APPS = INSTALLED_APPS + [
    'storages',
]

ALLOWED_HOSTS = ['diegopeluffo.com', 'www.diegopeluffo.com']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
USE_X_FORWARDED_HOST = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, # No deshabilitar loggers existentes (por ejemplo, los de Django)

    'formatters': { # Define cómo se verán los mensajes de log
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': { # Define a dónde irán los mensajes de log
        'console': { # Para ver logs en la consola (útil para contenedores Docker)
            'level': 'INFO', # Mostrar INFO, WARNING, ERROR, CRITICAL
            'class': 'logging.StreamHandler',
            'formatter': 'simple', # Usar formato simple
        },
        'file': { # Para guardar logs en un archivo (¡Recomendado para producción real!)
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler', # Rota el archivo para no llenar el disco
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'logs', 'django.log'), # Ruta del archivo de log
            'maxBytes': 1024*1024*5, # Tamaño máximo del archivo antes de rotar (5 MB)
            'backupCount': 5, # Número de archivos de respaldo a mantener
            'formatter': 'verbose', # Usar formato verbose
        },
        'mail_admins': { # Para enviar un email a los ADMINS en caso de errores CRÍTICOS
            'level': 'ERROR', # Solo errores y críticos
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True, # Incluir HTML del traceback si es un error HTTP
        }
    },
    'loggers': { # Define qué "loggers" hay en tu aplicación y qué handlers usarán
        'django': { # El logger principal de Django (para el framework)
            'handlers': ['console', 'file', 'mail_admins'], # Envía logs a consola, archivo y email si es error
            'level': 'INFO', # Nivel mínimo para el logger de Django
            'propagate': False, # Importante: evita que los logs de Django se propaguen al logger raíz si no quieres duplicarlos.
        },
        'django.request': { # Logger específico para errores de solicitud HTTP (4xx, 5xx)
            'handlers': ['console', 'file', 'mail_admins'],
            'level': 'ERROR', # Solo errores de solicitud
            'propagate': False,
        },
        'diegopeluffo_app': { # Ejemplo de un logger para tu propia aplicación personalizada
            'handlers': ['console', 'file'],
            'level': 'INFO', # Puedes ajustar este nivel (DEBUG, INFO, WARNING, ERROR)
            'propagate': False,
        },
    },
    'root': { # El logger raíz (captura todo lo que no es capturado por un logger específico)
        'handlers': ['console', 'file'], # Puedes añadir 'mail_admins' aquí también
        'level': 'WARNING', # Nivel mínimo para el logger raíz
    }
}

ADMINS = [
    ('mavergarah', 'mavergarah@gmail.com'),
]
MANAGERS = ADMINS # O puedes definir un grupo diferente si es necesario

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')          # Ej: 'smtp.sendgrid.net' o 'smtp.mailgun.org'
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587)) # Puerto estándar para TLS (587) o SSL (465)
EMAIL_USE_TLS = True                               # Usar TLS si el puerto es 587. Si usas 465, podría ser EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') # Usuario SMTP (ej: 'apikey' para SendGrid, o tu usuario de Mailgun)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') # Contraseña SMTP (ej: tu API Key)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = 'public-read'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_LOCATION = 'media'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
