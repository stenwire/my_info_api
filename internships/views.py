import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class HNGListView(APIView):
    def get(self, *args, **kwargs):
        data = {
        "slackUsername": "Rogue_Astronaut",
        "backend": True,
        "age": 31,
        "bio": "I love to tinker"
        }
        return JsonResponse(data, status=status.HTTP_200_OK)
