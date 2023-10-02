from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user).order_by('-priority')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
