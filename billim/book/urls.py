from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name="book_list"),
    path('<int:pk>/', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<int:pk>', edit, name="edit"),
    path('update/<int:pk>', update, name="update"),
    path('delete/<int:pk>', delete, name="delete"),
]
