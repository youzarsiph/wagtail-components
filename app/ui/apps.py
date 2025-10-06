"""AppConf for app.ui"""

from django.apps import AppConfig


# Create your config here.
class UIConfig(AppConfig):
    """App configuration for app.ui"""

    name = "app.ui"
    label = "app_ui"
    default_auto_field = "django.db.models.BigAutoField"
