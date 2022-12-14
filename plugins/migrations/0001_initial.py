# Generated by Django 4.1.1 on 2022-10-29 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PluginsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Наименования категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Plugins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('id_in_rep', models.IntegerField(blank=True, default=0, verbose_name='Id в репозитории')),
                ('module_name', models.CharField(blank=True, max_length=150, verbose_name='Имя модуля')),
                ('version', models.IntegerField(default=1, verbose_name='Версия')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активирован')),
                ('is_migrate', models.BooleanField(default=False, verbose_name='Миграция')),
                ('related_class_name', models.CharField(blank=True, max_length=150, verbose_name='Имя класса для связи')),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='get_category', to='plugins.pluginscategory', verbose_name='Категория')),
                ('related', models.ManyToManyField(to='plugins.plugins')),
            ],
            options={
                'verbose_name': 'Плагин',
                'verbose_name_plural': 'Плагины',
                'ordering': ['title'],
            },
        ),
    ]
