from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='user_library'),
    path('create-set/', views.create_set_view, name='create_set'),
    path('create-new-set/', views.create_new_set_view, name='create_new_set'),
    path('set-<slug:set_slug>/', views.set_view, name='set'),
    path('set-<slug:set_slug>/delete-set-confirm/', views.delete_set_confirm_view, name='delete_set_confirm'),
    path('set-<slug:set_slug>/delete-set/', views.delete_set, name='delete_set'),
    path('set-<slug:set_slug>/rename-set/', views.rename_set_view, name='rename_set'),
    path('set-<slug:set_slug>/create-card/', views.create_card_view, name='create_card'),
    path('set-<slug:set_slug>/cards/', views.set_cards_view, name='set_cards'),
    path('set-<slug:set_slug>/cards/delete-card-<int:card_id>/', views.delete_card, name='delete_card'),
    path('set-<slug:set_slug>/cards/edit-card-<int:card_id>/', views.edit_card_view, name='edit_card'),
    path('set-<slug:set_slug>/share-set/', views.share_set_view, name='share_set'),
    path('set-<slug:set_slug>/share-set-success/', views.share_set_success_view, name='share_set_success'),
    path('set-<slug:set_slug>/learn-cards/', views.learn_cards_view, name='learn_cards'),
]