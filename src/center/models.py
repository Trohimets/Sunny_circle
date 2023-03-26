from django.core.validators import FileExtensionValidator
from django.db import models
from django.shortcuts import reverse
from pytils.translit import slugify

from src.assistance.models import Job
from src.main_page.models import MainPage


class CenterPage(models.Model):
    """
    Модель страницы Центр
    """
    title = models.CharField(
        max_length=100,
        help_text='Введите название страницы',
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=700,
        help_text='Введите описание страницы',
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='center_page_images/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        help_text='Выберите изображение',
        verbose_name='Изображение'
    )
    opening_year = models.PositiveSmallIntegerField(
        help_text='Введите год открытия',
        verbose_name='Год открытия'
    )
    children_number = models.PositiveSmallIntegerField(
        help_text='Введите количество детей',
        verbose_name='Количество детей'
    )
    families_number = models.PositiveSmallIntegerField(
        help_text='Введите количество семей',
        verbose_name='Количество семей'
    )
    main_page = models.OneToOneField(
        MainPage,
        verbose_name='Главная страница',
        related_name='center_page',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Страница "Центр"'
        verbose_name_plural = 'Страница "Центр"'
        db_table = 'CenterPage'

    def __str__(self):
        return self.title


class CenterSectionPage(models.Model):
    """
    Базовая модель для страниц раздела Центр
    """
    title = models.CharField(
        max_length=100,
        help_text='Введите название',
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=700,
        help_text='Введите описание',
        verbose_name='Описание'
    )
    block_description = models.TextField(
        max_length=350,
        help_text='Введите краткое описание',
        verbose_name='Краткое описание'
    )
    image = models.ImageField(
        upload_to='center_section_page_images/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        help_text='Выберите изображение',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title


class School(CenterSectionPage):
    """
    Модель страницы Школа
    """

    class Meta:
        verbose_name = 'Страница "Школа"'
        verbose_name_plural = 'Страница "Школа"'
        db_table = 'School'


class Workshops(CenterSectionPage):
    """
    Модель страницы Мастерские
    """

    class Meta:
        verbose_name = 'Страница "Мастерские"'
        verbose_name_plural = 'Страница "Мастерские"'
        db_table = 'Workshops'


class Kindergarten(CenterSectionPage):
    """
    Модель страницы Сад
    """

    class Meta:
        verbose_name = 'Страница "Сад"'
        verbose_name_plural = 'Страница "Сад"'
        db_table = 'Kindergarten'


class Eis(CenterSectionPage):
    """
    Модель страницы Служба Раннего Вмешательства
    """

    class Meta:
        verbose_name = 'Страница "Служба Раннего Вмешательства"'
        verbose_name_plural = 'Страница "Служба Раннего Вмешательства"'
        db_table = 'Eis'


class SpecialistsPage(models.Model):
    """
    Модель страницы Cпециалисты
    """
    title = models.CharField(
        max_length=100,
        help_text='Введите заголовок',
        verbose_name='Заголовок'
    )
    description = models.TextField(
        max_length=700,
        help_text='Введите описание',
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='center_section_page_images/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        help_text='Выберите изображение',
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Страница "Специалисты"'
        verbose_name_plural = 'Страница "Специалисты"'
        db_table = 'SpecialistsPage'

    def __str__(self):
        return self.title


class Specialist(models.Model):
    """
    Модель специалиста
    """
    image = models.ImageField(
        upload_to='center_section_page_images/specialists/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        help_text='Выберите изображение',
        verbose_name='Изображение'
    )
    last_name = models.CharField(
        max_length=150,
        help_text='Введите фамилию',
        verbose_name='Фамилия'
    )
    first_name = models.CharField(
        max_length=150,
        help_text='Введите имя',
        verbose_name='Имя'
    )
    middle_name = models.CharField(
        max_length=150,
        blank=True,
        help_text='Введите отчество',
        verbose_name='Отчество'
    )
    position = models.TextField(
        max_length=700,
        help_text='Введите должность',
        verbose_name='Должность'
    )
    slug = models.SlugField(
        max_length=90,
        unique=True,
        db_index=True,
        verbose_name='Слаг'
    )
    info = models.TextField(
        max_length=1000,
        help_text='Введите информацию о специалисте',
        verbose_name='Информация о специалисте'
    )

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
        db_table = 'Specialist'

    def __str__(self):
        return f'ФИО: {self.full_name}, Должность: {self.position}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def get_absolute_url(self):
        return reverse('/center/specialists/', kwargs={'slug': self.slug})


class VolunteersPage(models.Model):
    """
    Модель страницы Волонтеры
    """
    title = models.CharField(
        max_length=100,
        help_text='Введите заголовок страницы',
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=700,
        help_text='Введите описание страницы',
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='volunteers_page_images/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        help_text='Выберите изображение',
        verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Страница "Волонтеры"'
        verbose_name_plural = 'Страница "Волонтеры"'
        db_table = 'VolunteersPage'

    def __str__(self):
        return self.title


class Volunteer(models.Model):
    """
    Модель волонтеров
    """
    image = models.ImageField(
        upload_to='center_section_page_images/volunteers/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        blank=True,
        null=True,
        help_text='Выберите изображение',
        verbose_name='Изображение'
    )
    first_name = models.CharField(
        max_length=150,
        help_text='Введите имя',
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        help_text='Введите фамилию',
        verbose_name='Фамилия'
    )
    middle_name = models.CharField(
        max_length=150,
        blank=True,
        help_text='Введите отчество',
        verbose_name='Отчество'
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        help_text='Введите адрес электронной почты',
        verbose_name='Электронная почта'
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
        help_text='Введите номер телефона',
        verbose_name='Телефон'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.PROTECT,
        related_name='volunteers',
        verbose_name='Работа'
    )
    filing_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата подачи заявки'
    )

    class Meta:
        verbose_name = 'Волонтер',
        verbose_name_plural = 'Волонтеры'
        db_table = 'Volunteer'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class EducationalSite(models.Model):
    """
    Модель ссылки образовательного сайта
    """
    url = models.URLField(
        max_length=200,
        help_text='Введите ссылку на образовательный сайт',
        verbose_name='Ссылка на образовательный сайт'
    )

    class Meta:
        verbose_name = 'Образовательный сайт'
        verbose_name_plural = 'Образовательный сайт'
        db_table = 'EducationalSite'

    def __str__(self):
        return self.url
