# Generated by Django 4.1.4 on 2023-01-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalCookies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_uid', models.CharField(max_length=255, unique=True)),
                ('approval_at', models.DateTimeField(auto_now_add=True)),
                ('user_agent', models.CharField(max_length=255)),
            ],
        ),
    ]