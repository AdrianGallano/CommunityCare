from django.shortcuts import render
from django.urls import reverse_lazy

from rest_framework.decorators import api_view
from django.http import HttpResponsePermanentRedirect


def index(request):
    return HttpResponsePermanentRedirect(reverse_lazy("core:docs"))