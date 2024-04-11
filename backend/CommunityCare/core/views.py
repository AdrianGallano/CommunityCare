from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view
from django.http import HttpResponsePermanentRedirect
from .serializers import FamilySerializer
from .models import Family

@api_view()
def docs(request):
    return Response({"sample":"test"}, status=status.HTTP_200_OK)


class FamiliesViewSet(ViewSet):
    def list(self, request, pk=None):
        families = Family.objects.all()
        
        title = request.query_params.get("title")
        if title:
            families = families.filter(title__contains=title)

        serialized_item = FamilySerializer(families, many=True)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    
    def create(self, request, pk=None):
        deserialized_item = FamilySerializer(request.data)
        if not deserialized_item.is_valid(raise_exception=True):
            return Response(deserialized_item.errors, status=status.HTTP_400_BAD_REQUEST) 
        return Response(deserialized_item.data, status=status.HTTP_201_CREATED)
    


class SingleFamilyViewSet(ViewSet):
    def retrieve(self, request, pk=None):

        family = Family.objects.get(pk=pk)
        serialized_item = FamilySerializer(family)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    
