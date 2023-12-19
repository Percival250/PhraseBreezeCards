from django.urls import path
from .views import info_list_view

urlpatterns = [
    path('info_list/', info_list_view)
]