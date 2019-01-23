# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import status
from . import serializers
from . import models
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retorna una lista de caracteristicas de APIView"""

        an_apiview = [
            "usa metodos HTTP como funcion (get, post, putch, put, delete)",
            "Esto es similar a una vista tradicional de Django",
            "Te da el mayor control sobre tu lógica",
            "Es mapeado manualmente para URLS"
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea un mensaje de saludo con un nombre"""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Maneja la actualizacion de un objeto"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Actualiza campos provisto de un objeto"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """borra un objeto"""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """retorna un hello mensaje"""

        a_viewset = [
            "User actions (list, create, retrieve, update, partial_update)",
            "Mapea automáticamente a URLs usando Routers",
            "Provee mas funcionalidad con menos código"
        ]

        return Response({'mesagge': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """crea un saludo de mensaje"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """manejador obtiene un objeto por su ID"""

        return Response({'http_method': "GET"})

    def update(self, request, pk=None):
        """manejador actualiza un objeto por su ID"""

        return Response({'http_method': "put"})

    def partial_update(self, request, pk=None):
        """manejador actualiza parte un objeto por su ID"""

        return Response({'http_method': "patch"})

    def destroy(self, request, pk=None):
        """manejador borra un objeto por su ID"""

        return Response({'http_method': "delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Crea y actualiza profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.MyUser.objects.all()
