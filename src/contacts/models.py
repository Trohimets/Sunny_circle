from django.db import models

from src.assistance.models import ReportType
from src.center.models import (CenterPage,
                               School,
                               Eis,
                               Workshops,
                               Kindergarten,
                               SpecialistsPage,
                               VolunteersPage,
                               Specialist)
from src.main_page.models import MainPage


class ContactsPage(models.Model):
    """
    Модель страницы Контакты
    """
    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True,
        help_text='Введите адрес',
        verbose_name='Адрес'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        help_text='Введите номер телефона',
        verbose_name='Телефон'
    )
    email = models.EmailField(
        blank=True,
        null=True,
        unique=True,
        help_text='Введите адрес электронной почты',
        verbose_name='Электронная почта'
    )
    working_time = models.CharField(
        max_length=16,
        blank=True,
        help_text='Введите рабочее время',
        verbose_name='Рабочее время'
    )
    working_day = models.CharField(
        max_length=25,
        blank=True,
        help_text='Введите рабочие дни',
        verbose_name='Рабочие дни'
    )

    class Meta:
        verbose_name = 'Страница "Контакты"'
        verbose_name_plural = 'Страница "Контакты"'
        db_table = 'ContactsPage'
