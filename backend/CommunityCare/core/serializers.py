from rest_framework import serializers
from .models import Citizenship, Location, Family, Member, MaritalStatus, EducationalAttainment,EmployementStatus


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["address", "coordinates"]

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ["title", "no_of_members", "total_family_income", "duration_of_residence",  "location"]
        depth = 1

class CitizenshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizenship
        fields = ["title"]

class EducationalAttainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalAttainment
        fields = ["title"]

class EmployementStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployementStatus
        fields = ["title"]

class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ["title"]

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = Member
        fields = ["name", "age", "contact_no", "income", "birthdate", "birth_place", "marital_status", "citizenship", "educatinal_attainment", "employement_status", "family"]
