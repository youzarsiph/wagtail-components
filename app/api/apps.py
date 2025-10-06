"""AppConf for app.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for app.api"""

    name = "app.api"
    label = "app_api"
    default_auto_field = "django.db.models.BigAutoField"
