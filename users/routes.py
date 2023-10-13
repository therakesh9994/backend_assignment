from django.urls import path
from .apis import RegistrationView

urlpatterns = [
    path('api/register/', RegistrationView.as_view(), name="sign_up"),
]
