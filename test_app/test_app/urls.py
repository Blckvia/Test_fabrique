from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('api.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
]

urlpatterns += doc_url
