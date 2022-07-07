import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpeg', '.jpg']
    if not ext.lower() in valid_extensions:
        raise Exception('Unsupported file extension.')


def icon_file_path(instance, filename):
    return f"icons/{filename}"
