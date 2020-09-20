from django.urls import path, include
from django.contrib import admin
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.accounts.urls')),
    path('api/v1/', include('api.inventory.urls')),
    path('api/v1/', include('api.orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
