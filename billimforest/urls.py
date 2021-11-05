from django.urls import path
from .views import *

urlpatterns = [
    path('notice/', notice, name="notice"),
    path('guide/', guide, name="guide"),
    path('producer/', producer, name="producer"),
]
