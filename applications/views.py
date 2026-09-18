from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets

from .models import Application
from .serializers import ApplicationSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = [
        "status",
        "job_type",
    ]

    search_fields = [
        "company",
        "position",
    ]

    ordering_fields = [
        "created_at",
        "applied_on",
        "expected_salary",
    ]

    def get_queryset(self):
        return Application.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)