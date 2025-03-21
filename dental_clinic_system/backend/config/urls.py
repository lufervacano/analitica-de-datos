from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', include('authentication.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/anamnesis/', include('anamnesis.urls')),
    path('api/stomatological-exam/', include('stomatological_exam.urls')),
    path('api/dental-exam/', include('dental_exam.urls')),
    path('api/odontogram/', include('odontogram.urls')),
    path('api/diagnosis/', include('diagnosis.urls')),
    path('api/appointments/', include('appointments.urls')),
    path('api/finance/', include('finance.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
