import django_filters
from rest_framework import viewsets

from root.utils import StandardPagination, IsAuthenticatedOrOptions
from students.models import Student
from students.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'id_number']
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticatedOrOptions]
