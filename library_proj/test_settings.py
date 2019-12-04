from .settings import *          

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRESQL_DATABASE"),
        'HOST': 'test_postgresql-master_1',
        'PORT': 5432,
        'USER': os.getenv("POSTGRESQL_USERNAME"),
        'PASSWORD': os.getenv("POSTGRESQL_PASSWORD"),
    },
}

MIDDLEWARE.remove('django_replicated.middleware.ReplicationMiddleware')
