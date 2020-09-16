from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.accounts.urls')),
    path('api/v1/', include('api.inventory.urls')),
    path('api/v1/', include('api.orders.urls')),
]
