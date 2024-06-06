from rest_framework import serializers
from .models import (
    Citizenship,
    Family,
    Member,
    MaritalStatus,
    EducationalAttainment,
    EmploymentStatus,
)


class FamilySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Family
        fields = [
            "id",
            "title",
            "no_of_members",
            "total_family_income",
            "duration_of_residence",
            "address",
            "coordinates",
        ]
        depth = 1


class CitizenshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citizenship
        fields = ["id", "title"]


class EducationalAttainmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EducationalAttainment
        fields = ["id", "title"]


class EmploymentStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmploymentStatus
        fields = ["id", "title"]


class MaritalStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ["id", "title"]


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    marital_status_id = serializers.PrimaryKeyRelatedField(
        queryset=MaritalStatus.objects.all(), source="marital_status", write_only=True
    )
    citizenship_id = serializers.PrimaryKeyRelatedField(
        queryset=Citizenship.objects.all(), source="citizenship", write_only=True
    )
    educational_attainment_id = serializers.PrimaryKeyRelatedField(
        queryset=EducationalAttainment.objects.all(),
        source="educational_attainment",
        write_only=True,
    )
    employment_status_id = serializers.PrimaryKeyRelatedField(
        queryset=EmploymentStatus.objects.all(),
        source="employment_status",
        write_only=True,
    )
    family_id = serializers.PrimaryKeyRelatedField(
        queryset=Family.objects.all(), source="family", write_only=True, many=True
    )

    class Meta:
        depth = 1
        model = Member
        fields = [
            "id",
            "name",
            "age",
            "contact_no",
            "income",
            "gender",
            "birthdate",
            "birth_place",
            "marital_status",
            "citizenship",
            "educational_attainment",
            "employment_status",
            "family",
            "marital_status_id",
            "citizenship_id",
            "educational_attainment_id",
            "employment_status_id",
            "family_id",
        ]
