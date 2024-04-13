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


class LocationsViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    search_fields = ["address", "coordinates"]
    ordering_fields = ["address", "coordinates"]
    pagination_class = CustomPageNumberPagination

class SingleLocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class FamiliesViewSet(ModelViewSet):
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
    serializer_class = FamilySerializer
    queryset = Family.objects.all()


class CitizenshipsViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleCitizenshipViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()


class CitizenshipsViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleCitizenshipViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()


class EducationalAttainmentsViewSet(ModelViewSet):
    serializer_class = EducationalAttainmentSerializer
    queryset = EducationalAttainment.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleEducationalAttainmentViewSet(ModelViewSet):
    serializer_class = EducationalAttainmentSerializer
    queryset = EducationalAttainment.objects.all()


class EmploymentStatusesViewSet(ModelViewSet):
    serializer_class = EmploymentStatusSerializer
    queryset = EmploymentStatus.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleEmploymentStatusViewSet(ModelViewSet):
    serializer_class = EmploymentStatusSerializer
    queryset = EmploymentStatus.objects.all()


class MaritalStatusesViewSet(ModelViewSet):
    serializer_class = MaritalStatusSerializer
    queryset = MaritalStatus.objects.all()
    search_fields = ["title"]
    ordering_fields = ["title"]
    pagination_class = CustomPageNumberPagination


class SingleMaritalStatusViewSet(ModelViewSet):
    serializer_class = MaritalStatusSerializer
    queryset = MaritalStatus.objects.all()


class MembersViewSet(ModelViewSet):
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
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
