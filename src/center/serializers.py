from rest_framework.serializers import ModelSerializer

from .models import (VolunteersPage, CenterSectionPage, Volunteer, CenterPage,
                     SpecialistsPage, Specialist, EducationalSite)
from ..assistance.serializers import JobSerializer


class CenterSectionPageSerializer(ModelSerializer):
    class Meta:
        model = CenterSectionPage
        fields = (
            'id',
            'title',
            'description',
            'block_description',
            'image'
        )


class VolunteersListSerializer(ModelSerializer):
    job = JobSerializer()

    class Meta:
        model = Volunteer
        fields = (
            'image',
            'first_name',
            'last_name',
            'middle_name',
            'job'
        )


class VolunteersCreateSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'phone',
            'job'
        )


class EducationalSiteSerializer(ModelSerializer):
    class Meta:
        model = EducationalSite
        fields = (
            'id',
            'url'
        )


class CenterPageSerializer(ModelSerializer):
    class Meta:
        model = CenterPage
        fields = (
            'id',
            'title',
            'description',
            'image',
            'opening_year',
            'children_number',
            'families_number'
        )


class CenterPageForMainPageSerializer(ModelSerializer):
    class Meta:
        model = CenterPage
        fields = (
            'id',
            'opening_year',
            'children_number',
            'families_number'
        )


class VolunteersPageSerializer(ModelSerializer):
    class Meta:
        model = VolunteersPage
        fields = (
            'id',
            'title',
            'description',
            'image'
        )


class SpecialistsDetailSerializer(ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            'image',
            'first_name',
            'last_name',
            'middle_name',
            'position',
            'info',
        )
        lookup_field = 'slug'


class SpecialistsListSerializer(ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            'image',
            'first_name',
            'last_name',
            'middle_name',
            'position',
        )


class SpecialistsPageSerializer(ModelSerializer):
    class Meta:
        model = SpecialistsPage
        fields = (
            'title',
            'description',
            'image'
        )
