# Generated by Django 4.1.4 on 2023-01-13 17:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assistance', '0001_initial'),
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterSectionPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название', max_length=100, verbose_name='Название')),
                ('description', models.TextField(help_text='Введите описание', max_length=700, verbose_name='Описание')),
                ('block_description', models.TextField(help_text='Введите краткое описание', max_length=350, verbose_name='Краткое описание')),
                ('image', models.ImageField(help_text='Выберите изображение', upload_to='center_section_page_images/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='EducationalSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text='Введите ссылку на образовательный сайт', verbose_name='Ссылка на образовательный сайт')),
            ],
            options={
                'verbose_name': 'Образовательный сайт',
                'verbose_name_plural': 'Образовательный сайт',
                'db_table': 'EducationalSite',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Выберите изображение', upload_to='center_section_page_images/specialists/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Изображение')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=150, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, help_text='Введите отчество', max_length=150, verbose_name='Отчество')),
                ('position', models.TextField(help_text='Введите должность', max_length=700, verbose_name='Должность')),
                ('slug', models.SlugField(max_length=90, unique=True, verbose_name='Слаг')),
                ('info', models.TextField(help_text='Введите информацию о специалисте', max_length=1000, verbose_name='Информация о специалисте')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
                'db_table': 'Specialist',
            },
        ),
        migrations.CreateModel(
            name='SpecialistsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите заголовок', max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(help_text='Введите описание', max_length=700, verbose_name='Описание')),
                ('image', models.ImageField(help_text='Выберите изображение', upload_to='center_section_page_images/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Страница "Специалисты"',
                'verbose_name_plural': 'Страница "Специалисты"',
                'db_table': 'SpecialistsPage',
            },
        ),
        migrations.CreateModel(
            name='VolunteersPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите заголовок страницы', max_length=100, verbose_name='Название')),
                ('description', models.TextField(help_text='Введите описание страницы', max_length=700, verbose_name='Описание')),
                ('image', models.ImageField(help_text='Выберите изображение', upload_to='volunteers_page_images/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Страница "Волонтеры"',
                'verbose_name_plural': 'Страница "Волонтеры"',
                'db_table': 'VolunteersPage',
            },
        ),
        migrations.CreateModel(
            name='Eis',
            fields=[
                ('centersectionpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='center.centersectionpage')),
            ],
            options={
                'verbose_name': 'Страница "Служба Раннего Вмешательства"',
                'verbose_name_plural': 'Страница "Служба Раннего Вмешательства"',
                'db_table': 'Eis',
            },
            bases=('center.centersectionpage',),
        ),
        migrations.CreateModel(
            name='Kindergarten',
            fields=[
                ('centersectionpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='center.centersectionpage')),
            ],
            options={
                'verbose_name': 'Страница "Сад"',
                'verbose_name_plural': 'Страница "Сад"',
                'db_table': 'Kindergarten',
            },
            bases=('center.centersectionpage',),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('centersectionpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='center.centersectionpage')),
            ],
            options={
                'verbose_name': 'Страница "Школа"',
                'verbose_name_plural': 'Страница "Школа"',
                'db_table': 'School',
            },
            bases=('center.centersectionpage',),
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('centersectionpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='center.centersectionpage')),
            ],
            options={
                'verbose_name': 'Страница "Мастерские"',
                'verbose_name_plural': 'Страница "Мастерские"',
                'db_table': 'Workshops',
            },
            bases=('center.centersectionpage',),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Выберите изображение', null=True, upload_to='center_section_page_images/volunteers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Изображение')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=150, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, help_text='Введите отчество', max_length=150, verbose_name='Отчество')),
                ('email', models.EmailField(help_text='Введите адрес электронной почты', max_length=150, unique=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(help_text='Введите номер телефона', max_length=20, unique=True, verbose_name='Телефон')),
                ('filing_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи заявки')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='volunteers', to='assistance.job', verbose_name='Работа')),
            ],
            options={
                'verbose_name': ('Волонтер',),
                'verbose_name_plural': 'Волонтеры',
                'db_table': 'Volunteer',
            },
        ),
        migrations.CreateModel(
            name='CenterPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название страницы', max_length=100, verbose_name='Название')),
                ('description', models.TextField(help_text='Введите описание страницы', max_length=700, verbose_name='Описание')),
                ('image', models.ImageField(help_text='Выберите изображение', upload_to='center_page_images/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Изображение')),
                ('opening_year', models.PositiveSmallIntegerField(help_text='Введите год открытия', verbose_name='Год открытия')),
                ('children_number', models.PositiveSmallIntegerField(help_text='Введите количество детей', verbose_name='Количество детей')),
                ('families_number', models.PositiveSmallIntegerField(help_text='Введите количество семей', verbose_name='Количество семей')),
                ('main_page', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='center_page', to='main_page.mainpage', verbose_name='Главная страница')),
            ],
            options={
                'verbose_name': 'Страница "Центр"',
                'verbose_name_plural': 'Страница "Центр"',
                'db_table': 'CenterPage',
            },
        ),
    ]
