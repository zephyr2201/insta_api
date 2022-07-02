import os

from instagram.models import Content, Niche, Rubric


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpeg', '.jpg']
    if not ext.lower() in valid_extensions:
        raise Exception('Unsupported file extension.')


def create_rubric(name: str):
    Rubric.objects.create(name=name)


def create_content(name: str):
    Content.objects.create(name=name)


def create_niche(name: str):
    Niche.objects.create(name=name)
