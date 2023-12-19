from django.urls import path
from .views import lending_page_view

urlpatterns = [
    path('', lending_page_view, name = 'lending_page')
]