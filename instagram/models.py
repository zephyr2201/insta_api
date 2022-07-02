from django.db import models
from django.utils.translation import gettext_lazy as _

from instagram import LevelStates


class Niche(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name = _('Ниша')
        verbose_name_plural = _('Нишы')

    def __str__(self) -> str:
        return self.name


class Rubric(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name = _('Рубрика')
        verbose_name_plural = _('Рубрики')

    def __str__(self) -> str:
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name = _('Контент')
        verbose_name_plural = _('Контенты')

    def __str__(self) -> str:
        return self.name


class Text(models.Model):
    level = models.CharField(
        _('Уровень'),
        max_length=255,
        choices=LevelStates.choices,
        null=True
    )
    rubric = models.ForeignKey(
        verbose_name=_('Рубрика'),
        to=Rubric,
        on_delete=models.SET_NULL,
        related_name='text',
        null=True,
    )
    niche = models.ForeignKey(
        verbose_name=_('Ниша'),
        to=Niche,
        on_delete=models.SET_NULL,
        related_name='text',
        null=True,
    )
    content = models.ForeignKey(
        verbose_name=_('Контент'),
        to=Content,
        on_delete=models.SET_NULL,
        related_name='text',
        null=True,
    )
    body = models.TextField(
        _('Текст для поста'),
        null=True,
        blank=True
        )
