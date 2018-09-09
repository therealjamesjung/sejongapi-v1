from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'student_id', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
