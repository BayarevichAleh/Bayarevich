# Generated by Django 3.1 on 2020-09-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.DateField(blank=True, null=True, verbose_name='Дата Рождения'),
        ),
    ]