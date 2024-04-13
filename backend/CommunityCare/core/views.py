from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, FamilySerializer, CitizenshipSerializer, MemberSerializer, EducationalAttainmentSerializer, EmploymentStatusSerializer, MaritalStatusSerializer, MemberSerializer
from .models import Location, Family, Citizenship, EducationalAttainment, EmploymentStatus, MaritalStatus, Member

class LocationsViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class SingleLocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class FamiliesViewSet(ModelViewSet):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()


class SingleFamilyViewSet(ModelViewSet):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()

class CitizenshipsViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()


class SingleCitizenshipViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()

class CitizenshipsViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()


class SingleCitizenshipViewSet(ModelViewSet):
    serializer_class = CitizenshipSerializer
    queryset = Citizenship.objects.all()

class EducationalAttainmentsViewSet(ModelViewSet):
    serializer_class = EducationalAttainmentSerializer
    queryset = EducationalAttainment.objects.all()

class SingleEducationalAttainmentViewSet(ModelViewSet):
    serializer_class = EducationalAttainmentSerializer
    queryset = EducationalAttainment.objects.all()

class EmploymentStatusesViewSet(ModelViewSet):
    serializer_class = EmploymentStatusSerializer
    queryset = EmploymentStatus.objects.all()

class SingleEmploymentStatusViewSet(ModelViewSet):
    serializer_class = EmploymentStatusSerializer
    queryset = EmploymentStatus.objects.all()

class MaritalStatusesViewSet(ModelViewSet):
    serializer_class = MaritalStatusSerializer
    queryset = MaritalStatus.objects.all()

class SingleMaritalStatusViewSet(ModelViewSet):
    serializer_class = MaritalStatusSerializer
    queryset = MaritalStatus.objects.all()

class MembersViewSet(ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class SingleMemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
