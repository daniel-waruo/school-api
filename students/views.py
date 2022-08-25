import django_filters
from rest_framework import viewsets

from root.utils import StandardPagination, IsAuthenticatedOrOptions
from students.models import Student, Activity
from students.serializers import StudentSerializer, ActivitySerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'id_number']
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticatedOrOptions]


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', ]
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticatedOrOptions]
