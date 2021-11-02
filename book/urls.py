from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name="book_list"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]