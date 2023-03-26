from rest_framework.viewsets import ReadOnlyModelViewSet

from src.assistance.models import Job, ReportType
from src.assistance.serializers import JobSerializer, ReportTypeSerializer


class JobViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра списка работ
    '''
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ReportTypeViewSet(ReadOnlyModelViewSet):
    '''
    Класс для просмотра информации страницы Отчеты
    '''
    queryset = ReportType.objects.all()
    serializer_class = ReportTypeSerializer
