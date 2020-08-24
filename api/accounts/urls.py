from django.urls import include, path
from rest_framework import routers
from rest_auth.views import PasswordResetConfirmView
from .views import UserViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path('user/registration', include('rest_auth.registration.urls')),
    path('user/', include('rest_auth.urls')),
    path(
        r'^user/password/reset/confirm/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    
]
