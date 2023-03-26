from rest_framework.serializers import ModelSerializer

from .models import MainPage
from ..center.serializers import CenterPageForMainPageSerializer


class MainPageSerializer(ModelSerializer):
    center_page = CenterPageForMainPageSerializer()

    class Meta:
        model = MainPage
        fields = (
            'id',
            'about_center_title',
            'about_center_description',
            'video',
            'center_page'
        )
