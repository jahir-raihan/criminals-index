from django.urls import path
from .views import *

urlpatterns = [
    path("", CriminalsList.as_view(), name='home')
]