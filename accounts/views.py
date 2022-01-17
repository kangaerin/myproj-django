from rest_framework_simplejwt.views import (
    TokenObtainPairView as OrigTokenObtainPairView,
    TokenRefreshView as OrigTokenRefreshView,
)
from accounts.serializer import TokenObtainPairSerializer


class TokenObtainPairView(OrigTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OrigTokenRefreshView):
    pass
