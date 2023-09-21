from .base import *
import environ

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))


SECRET_KEY = env.str("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT")
    }
}
