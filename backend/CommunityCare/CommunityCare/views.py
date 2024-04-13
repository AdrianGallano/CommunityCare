from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponsePermanentRedirect


def index(request):
    return HttpResponsePermanentRedirect(reverse_lazy("docs"))


@api_view()
def docs(request):
    return Response({"sample":"test"}, status=status.HTTP_200_OK)