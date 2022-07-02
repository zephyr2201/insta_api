from django.db.models import TextChoices


class LevelStates(TextChoices):
    TOP = "TOP", "Верхний"
    MIDDLE = "MIDDLE", "Срдений"
    BOT = "BOT", "Нижний"
