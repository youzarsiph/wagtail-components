"""URLConf for app.ui"""

from django.urls import path

from app.ui import views

# Create your URLConf here.
app_name = "app"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
]
