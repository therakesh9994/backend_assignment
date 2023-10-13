from django.urls import path
from .apis import PostCreateView

urlpatterns = [
    path('api/create/', PostCreateView.as_view(), name="post_create"),
]
