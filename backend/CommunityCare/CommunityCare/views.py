from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from django.http import HttpResponsePermanentRedirect
from rest_framework.renderers import TemplateHTMLRenderer

@api_view(["GET"])
def index(request):
    return HttpResponsePermanentRedirect(reverse_lazy("docs"))


@api_view(["GET"])
@renderer_classes([TemplateHTMLRenderer])
def docs(request):
    return Response(template_name="docs.html",status=status.HTTP_200_OK)