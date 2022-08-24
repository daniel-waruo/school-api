from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission


class StandardPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    page_size_query_param = 'page_size'


class IsAuthenticatedOrOptions(BasePermission):
    safe_methods = ["OPTIONS", ]

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True
        return request.user.is_authenticated
