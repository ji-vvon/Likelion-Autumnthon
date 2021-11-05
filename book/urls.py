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
    # path('category/<str:slug>', category_page, name='category_page'),

    path('category/IT/', category_IT, name="category_IT"),
    path('category/society/', category_society, name="category_society"),
    path('category/science/', category_science, name="category_science"),
    path('category/art/', category_art, name="category_art"),
    path('category/etc/', category_etc, name="category_etc"),

    path('mybook/', mybook, name="mybook"),
    path('myborrowed_book/', myborrowed_book, name="myborrowed_book"),
    path('search/', search, name="search"),
    path('placeholder/', placeholder, name="placeholder"),
]
