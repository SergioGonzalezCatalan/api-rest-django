from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """serializar un nombre de campo para probar APIview."""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """un serializador para la objetos user profile"""

    class Meta:
        model = models.MyUser
        fields = ('id', 'email', 'password', 'date_of_birth')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Crea y retorna un nuevo usuario"""

        user = models.MyUser(
            email=validated_data['email'],
            date_of_birth=validated_data['date_of_birth'],
        )

        user.set_password(validated_data['password'])

        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializador para profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profiles', 'status_text', 'created_on')
        extra_kwargs = {'user_profiles': {'read_only': True}}
