# Generated by Django 3.1 on 2020-10-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Forum', '0005_auto_20201012_0728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name': 'Котегория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='forum',
            options={'ordering': ['-create_date'], 'verbose_name': 'Форум', 'verbose_name_plural': 'Форумы'},
        ),
        migrations.AlterField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(default=3, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
    ]
