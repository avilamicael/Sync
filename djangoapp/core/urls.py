from django.urls import path
from .views import UserCreateView
from .views import GoogleLogin, FacebookLogin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    # path('auth/facebook/', FacebookLogin.as_view(), name='facebook_login'),

]
