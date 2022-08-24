from django.urls import path

from .views import LoginView, SignUpView

urlpatterns = [
    path('login', LoginView.as_view(), name='teacher_login'),
    path('sign-up', SignUpView.as_view(), name='teacher_sign_up'),
]
