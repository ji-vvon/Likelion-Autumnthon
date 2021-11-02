from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('search', search, name='search'),
    path('create_comment/<str:id>', create_comment, name="create_comment"),
    path('create_re_comment/<int:id>/<str:comment_id>', create_re_comment, name="create_re_comment"),
    path('delete_comment/<int:id>/<int:comment_id>', delete_comment, name="delete_comment"),
]