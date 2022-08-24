from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        if User.objects.filter(username=attrs["email"]).exists():
            raise serializers.ValidationError("Email must be unique")
        return attrs

    def save(self, **kwargs):
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = User(
            username=email,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user


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
