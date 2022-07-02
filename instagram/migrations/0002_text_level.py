# Generated by Django 4.0.5 on 2022-06-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='level',
            field=models.CharField(choices=[('TOP', 'Верхний'), ('MIDDLE', 'Срдений'), ('BOT', 'Нижний')], max_length=255, null=True, verbose_name='Уровень'),
        ),
    ]