# Generated by Django 3.1 on 2020-10-21 06:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0010_auto_20201018_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Сообщение'),
        ),
    ]