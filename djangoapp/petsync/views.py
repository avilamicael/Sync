import logging
from rest_framework import viewsets, permissions
from .models import Pet
from .serializers import PetSerializer

# Obter o logger específico para o app petsync
logger = logging.getLogger('petsync')

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        pet = serializer.save(owner=self.request.user)
        logger.info(f"Pet criado: {pet.name} (ID: {pet.id}) pelo usuário {pet.owner.username}")

    def perform_update(self, serializer):
        pet = serializer.save()
        logger.info(f"Pet atualizado: {pet.name} (ID: {pet.id}) pelo usuário {pet.owner.username}")

    def perform_destroy(self, instance):
        logger.info(f"Pet excluído: {instance.name} (ID: {instance.id}) pelo usuário {instance.owner.username}")
        instance.delete()
