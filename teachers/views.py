# Create your views here.
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from teachers.serializers import LoginSerializer, TokenSerializer


class LoginView(generics.GenericAPIView):
    """ Allow the teacher to login using their email as the username
    """
    http_method_names = ['post']
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token, is_created = Token.objects.get_or_create(user=serializer.save())
            serializer = TokenSerializer(instance=token)
            return Response(
                data={
                    'message': 'Login successful',
                    'data': serializer.data,
                    'success': True
                }
            )
        return Response(
            status=400,
            data={
                'message': 'Login failed',
                'success': False,
                'data': serializer.errors
            }
        )
