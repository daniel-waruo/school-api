from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        try:
            user = User.objects.get(username=attrs["email"])
            if user.check_password(attrs['password']):
                self.user = user
                return attrs
        except User.DoesNotExist:
            pass
        raise serializers.ValidationError("Invalid Credentials! Please try again.")

    def save(self, **kwargs):
        return self.user


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
