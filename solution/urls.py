from django.urls import path
from .views import *

urlpatterns = [
    path('', solution_home, name="solution_home"),
    path('solution_detail/<str:id>', solution_detail, name="solution_detail"),
    path('solution_new/', solution_new, name="solution_new"),
    path('solution_update/<str:id>', solution_update, name="solution_update"),
    path('solution_delete/<str:id>', solution_delete, name="solution_delete"),
    path('solution_search', solution_search, name='solution_search'),
    path('create_comment/<str:id>', create_comment, name="create_comment"),
    path('create_re_comment/<int:id>/<str:comment_id>', create_re_comment, name="create_re_comment"),
    path('delete_comment/<int:id>/<int:comment_id>', delete_comment, name="delete_comment"),
]