from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name="book_list"),
    path('detail/<int:pk>', detail, name="detail"),
    path('new/', new, name="new"),
    path('rental/<str:id>', rental, name="rental"),
    path('edit/<int:pk>', edit, name="edit"),
    path('update/<int:pk>', update, name="update"),
    path('delete/<int:pk>', delete, name="delete"),
    path('mypage/', mypage, name="mypage"),
]
