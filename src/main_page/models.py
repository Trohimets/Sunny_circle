from django.db import models


class MainPage(models.Model):
    """
    Модель главной страницы
    """
    about_center_title = models.CharField(
        max_length=100,
        help_text='Введите название блока "О центре"',
        verbose_name='Название блока "О центре"')
    about_center_description = models.TextField(
        max_length=700,
        help_text='Введите описание блока "О центре"',
        verbose_name='Описание блока "О центре"'
    )
    video = models.FileField(
        max_length=254,
        upload_to='main_page_videos/%Y/%m/%d/',
        help_text='Выберите видео',
        verbose_name='Видео'
    )

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
        db_table = 'MainPage'

    def __str__(self):
        return self.about_center_title
