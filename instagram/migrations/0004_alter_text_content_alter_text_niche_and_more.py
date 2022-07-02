# Generated by Django 4.0.5 on 2022-06-30 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_text_body_alter_content_name_alter_niche_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='text', to='instagram.content', verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='text',
            name='niche',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='text', to='instagram.niche', verbose_name='Ниша'),
        ),
        migrations.AlterField(
            model_name='text',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='text', to='instagram.rubric', verbose_name='Рубрика'),
        ),
    ]
