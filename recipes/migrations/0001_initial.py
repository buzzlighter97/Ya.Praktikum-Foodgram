# Generated by Django 3.1.5 on 2021-02-02 16:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import recipes.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('dimension', models.CharField(max_length=16, verbose_name='Eдиница измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='IngredientAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=1, max_digits=6, validators=[django.core.validators.MinValueValidator(0, 1)], verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Количество ингредиента',
                'verbose_name_plural': 'Количество ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('duration', models.SmallIntegerField(verbose_name='Время приготовления')),
                ('text', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(upload_to='recipe_images/', validators=[recipes.validators.validate_file_size], verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Завтрак', 'Завтрак'), ('Обед', 'Обед'), ('Ужин', 'Ужин')], max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(default='', editable=False, verbose_name='Адрес')),
                ('color', models.CharField(default='', editable=False, max_length=50, verbose_name='Цвет')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='recipes.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
    ]
