from django.core.validators import FileExtensionValidator
from django.db import models

from src.base.services import get_path_upload_report_file


class ReportType(models.Model):
    """
    Модель типов отчетов
    """
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text='Введите наименование',
        verbose_name='Наименование'
    )

    class Meta:
        verbose_name = 'Тип отчета'
        verbose_name_plural = 'Типы отчетов'
        db_table = 'ReportType'

    def __str__(self):
        return self.name


class Report(models.Model):
    """
    Модель отчетов
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Введите наименование',
        verbose_name='Название отчета'
    )
    file = models.FileField(
        max_length=254,
        upload_to=get_path_upload_report_file,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text='Выберите файл',
        verbose_name='Файл'
    )
    reporttype_id = models.ForeignKey(
        ReportType,
        on_delete=models.PROTECT,
        verbose_name='Тип отчета',
        related_name='reports'
    )

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
        db_table = 'Report'

    def __str__(self):
        return self.name


class Job(models.Model):
    """
    Модель работ
    """
    name = models.TextField(
        max_length=500,
        unique=True,
        help_text='Введите наименование',
        verbose_name='Наименование'
    )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        db_table = 'Job'

    def __str__(self):
        return self.name
