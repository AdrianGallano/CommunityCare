from django.urls import path, include
from . import views


app_name = "core"
urlpatterns = [
    path("docs", views.docs, name="docs"),
    path("family", views.FamiliesViewSet.as_view({
        "get":"list",
        "post":"create"
         
         }), name="families"),
    path("family/<int:pk>", views.SingleFamilyViewSet.as_view({
        "get":"retrieve"
    }), name="family"),



]