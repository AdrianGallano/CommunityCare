from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view()
def index(request):
    return Response({"All good"}, status=status.HTTP_200_OK)   