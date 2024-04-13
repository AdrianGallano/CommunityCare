from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    LocationSerializer,
    FamilySerializer,
    CitizenshipSerializer,
    MemberSerializer,
    EducationalAttainmentSerializer,
    EmploymentStatusSerializer,
    MaritalStatusSerializer,
    MemberSerializer,
)
from .models import (
    Location,
    Family,
    Citizenship,
    EducationalAttainment,
    EmploymentStatus,
    MaritalStatus,
    Member,
)
from .paginations import CustomPageNumberPagination
from rest_framework.permissions import IsAuthenticated

class LocationsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    search_fields = ["address", "coordinates"]
    ordering_fields = ["address", "coordinates"]
    pagination_class = CustomPageNumberPagination

class SingleLocationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class FamiliesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FamilySerializer
    queryset = Family.objects.all()
    pagination_class = CustomPageNumberPagination

    search_fields = [
        "title",
        "no_of_members",
        "total_family_income",
        "duration_of_residence",
        "location__address",
        "location__coordinates",
    ]
    ordering_fields = [
        "title",
        "no_of_members",
        "total_family_income",
        "duration_of_residence",
        "location__address",
        "location__coordinates",
    ]


class SingleFamilyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FamilySerializer
    queryset = Family.objects.all()

class CitizenshipsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleCitizenshipViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()


class CitizenshipsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleCitizenshipViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()


class EducationalAttainmentsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationalAttainmentSerializer
    queryset = EducationalAttainment.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleEducationalAttainmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationalAttainmentSerializer
    queryset = EducationalAttainment.objects.all()


class EmploymentStatusesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmploymentStatusSerializer
    queryset = EmploymentStatus.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleEmploymentStatusViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmploymentStatusSerializer
    queryset = EmploymentStatus.objects.all()


class MaritalStatusesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaritalStatusSerializer
    queryset = MaritalStatus.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleMaritalStatusViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MaritalStatusSerializer
    queryset = MaritalStatus.objects.all()


class MembersViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    search_fields = [
        "name",
        "age",
        "contact_no",
        "income",
        "gender",
        "birthdate",
        "birth_place",
        "marital_status__title",
        "citizenship__title",
        "educational_attainment__title",
        "employment_status__title",
        "family__title",
        "family__no_of_members",
        "family__total_family_income",
        "family__duration_of_residence",
        "family__location__address",
        "family__location__coordinates",
    ]
    ordering_fields = [
        "name",
        "age",
        "contact_no",
        "income",
        "gender",
        "birthdate",
        "birth_place",
        "marital_status__title",
        "citizenship__title",
        "educational_attainment__title",
        "employment_status__title",
        "family__title",
        "family__no_of_members",
        "family__total_family_income",
        "family__duration_of_residence",
        "family__location__address",
        "family__location__coordinates",
    ]
    pagination_class = CustomPageNumberPagination




class SingleMemberViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
