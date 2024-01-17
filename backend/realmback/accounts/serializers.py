from rest_framework import serializers
from .models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ['id', 'name', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Password do not match')
        return data

    def create(self, validated_data):
        user = UserAccount(
            name=validated_data['name'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
