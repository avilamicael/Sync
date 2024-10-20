from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),  # Endpoints de autenticação
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Endpoints de registro

    path('api/core/', include('core.urls')),
    path('api/petsync/', include('petsync.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
