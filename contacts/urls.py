from django.urls import path
from .views import contacts_list_view

urlpatterns = [
    path('contacts_list/', contacts_list_view)
]