"""AppConf for app.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for app.cms"""

    name = "app.cms"
    label = "app_cms"
    default_auto_field = "django.db.models.BigAutoField"
