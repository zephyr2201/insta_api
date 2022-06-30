# Generated by Django 4.0.5 on 2022-06-30 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контенты',
            },
        ),
        migrations.CreateModel(
            name='Niche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Ниша',
                'verbose_name_plural': 'Нишы',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text', to='instagram.content', verbose_name='Контент')),
                ('niche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text', to='instagram.niche', verbose_name='Ниша')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text', to='instagram.rubric', verbose_name='Рубрика')),
            ],
        ),
    ]
