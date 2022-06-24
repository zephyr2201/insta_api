import os
from rest_framework.serializers import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpeg', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')