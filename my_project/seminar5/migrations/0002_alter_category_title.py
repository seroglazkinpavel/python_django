# Generated by Django 4.2.4 on 2023-09-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=225, unique=True, verbose_name='Имя категории'),
        ),
    ]
