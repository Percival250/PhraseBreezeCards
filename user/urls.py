from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('delete-account-confirm/', views.delete_account_confirm_view, name='delete_account_confirm'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('change-password/', views.change_password_view, name='change_password'),
]
