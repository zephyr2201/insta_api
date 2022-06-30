from django.db import models
from django.utils.translation import gettext_lazy as _


class Niche(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = _('Ниша')
        verbose_name_plural = _('Нишы')

    def __str__(self) -> str:
        return self.name


class Rubric(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = _('Рубрика')
        verbose_name_plural = _('Рубрики')

    def __str__(self) -> str:
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = _('Контент')
        verbose_name_plural = _('Контенты')

    def __str__(self) -> str:
        return self.name


class Text(models.Model):
    rubric = models.ForeignKey(
        verbose_name=_('Рубрика'),
        to=Rubric,
        on_delete=models.CASCADE,
        related_name='text',
    )
    niche = models.ForeignKey(
        verbose_name=_('Ниша'),
        to=Niche,
        on_delete=models.CASCADE,
        related_name='text',
    )
    content = models.ForeignKey(
        verbose_name=_('Контент'),
        to=Content,
        on_delete=models.CASCADE,
        related_name='text',
    )
