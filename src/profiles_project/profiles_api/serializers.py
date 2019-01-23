from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializar un nombre de campo para probar APIview."""

    name = serializers.CharField(max_length=10)
