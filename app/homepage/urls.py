from django.urls import path
from .views import HomePage 


urlpatterns = [
    path("", HomePage, name="homepage"),
    path("accounts/profile/", HomePage),
]