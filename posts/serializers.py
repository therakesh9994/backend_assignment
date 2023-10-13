from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "user", "name", "description", "created_at", "updated_at"]

    def create(self, validated_data):
        return Post.objects.create(
            user=validated_data.get('user'),
            name=validated_data.get('name'),
            description=validated_data.get('description'),
        )
