from django.shortcuts import render
from django.http import JsonResponse
from .serializers import KeySerializer
from activation_keys.models import Key
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.


class KeyList(generics.ListAPIView):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = [permissions.AllowAny]


class AddKey(generics.CreateAPIView):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = [permissions.AllowAny]


class UpDelKey(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    # update key
    def put(self, request, key, *args, **kwargs):

        data = request.data  # dictionary
        account = data["account"]
        created = data["created"]
        try:
            updateKey = Key.objects.get(activation_key=key)
            updateKey.account = account
            updateKey.created_at = created
            updateKey.save()
            return Response({"message": "key successfully activated!"}, status=200)

        except:
            return Response({"error": "Invalid Key"}, status=404)

    # delete key
    def delete(self, request, key, *args, **kwargs):
        try:
            deleteKey = Key.objects.get(activation_key=key)
            deleteKey.delete()
            return Response({"message": "key successfully deleted!"}, status=200)
        except:
            return Response({"error": "Invalid Key"}, status=404)
