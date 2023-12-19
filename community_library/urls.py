from django.urls import path
from . import views


urlpatterns = [
    path('', views.library_view, name='community_library'),
    path('user=<slug:username>&set=<slug:set_slug>/', views.set_view, name='library_set'),
    path('user=<slug:username>&set=<slug:set_slug>/copy-set/', views.copy_set_view, name='copy_set'),

]
