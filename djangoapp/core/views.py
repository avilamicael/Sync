import logging
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Obter o logger específico para o app core
logger = logging.getLogger('core')

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        logger.info(f"Novo usuário registrado: {user.username} (ID: {user.id})")
