# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Retorna una lista de caracteristicas de APIView"""

        an_apiview = [
            "usa metodos HTTP como funcion (get, post, putch, put, delete)",
            "Esto es similar a una vista tradicional de Django",
            "Te da el mayor control sobre tu lógica",
            "Es mapeado manualmente para URLS"
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})
