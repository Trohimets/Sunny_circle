from rest_framework.serializers import ModelSerializer
from src.assistance.models import Job
from src.assistance.models import Report, ReportType


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'name')


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'name', 'file')


class ReportTypeSerializer(ModelSerializer):
    reports = ReportSerializer(many=True)

    class Meta:
        model = ReportType
        fields = ('id', 'name', 'reports')
