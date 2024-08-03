from django.urls import path
from .views import *

urlpatterns = [
    path("", CriminalsList.as_view(), name='home'),
    path("criminal-details/<int:pk>", CriminalsDetails.as_view(), name='criminal_details')
]