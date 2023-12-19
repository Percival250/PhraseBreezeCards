from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lending_page.urls')),
    path('your-library/', include('main_app.urls')),
    path('', include('authorization.urls')),
    path('', include('user.urls')),
    path('community-library/', include('community_library.urls')),
    path('', include('home.urls')),
    path('', include('about.urls')),
    path('', include('contacts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
