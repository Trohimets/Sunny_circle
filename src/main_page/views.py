from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import MainPage
from .serializers import MainPageSerializer


class MainPageViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации главной страницы
    '''
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
