# Generated by Django 4.2.4 on 2023-09-01 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamemodel',
            options={'ordering': ['-played']},
        ),
    ]
