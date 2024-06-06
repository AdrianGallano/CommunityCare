from django.urls import path
from . import views


urlpatterns = [
    path(
        "families",
        views.FamiliesViewSet.as_view({"get": "list", "post": "create"}),
        name="families",
    ),
    path(
        "families/<int:pk>",
        views.SingleFamilyViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="family-detail",
    ),
    path(
        "citizenships",
        views.CitizenshipsViewSet.as_view({"get": "list", "post": "create"}),
        name="citizenships",
    ),
    path(
        "citizenships/<int:pk>",
        views.SingleCitizenshipViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="citizenship-detail",
    ),
    path(
        "educational-attainments",
        views.EducationalAttainmentsViewSet.as_view({"get": "list", "post": "create"}),
        name="educational-attainments",
    ),
    path(
        "educational-attainments/<int:pk>",
        views.SingleEducationalAttainmentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="educationalattainment-detail",
    ),
    path(
        "employment-statuses",
        views.EmploymentStatusesViewSet.as_view({"get": "list", "post": "create"}),
        name="employment-statuses",
    ),
    path(
        "employment-statuses/<int:pk>",
        views.SingleEmploymentStatusViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="employmentstatus-detail",
    ),
    path(
        "marital-statuses",
        views.MaritalStatusesViewSet.as_view({"get": "list", "post": "create"}),
        name="marital-statuses",
    ),
    path(
        "marital-statuses/<int:pk>",
        views.SingleMaritalStatusViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="maritalstatus-detail",
    ),
    path(
        "members",
        views.MembersViewSet.as_view({"get": "list", "post": "create"}),
        name="members",
    ),
    path(
        "members/<int:pk>",
        views.SingleMemberViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="member-detail",
    ),
]
