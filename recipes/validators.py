from django.core.exceptions import ValidationError
from django import forms


def validate_file_size(image):
    filesize = image.size
    if filesize > 1000000:
        raise ValidationError(
            message=(
                'Максимальный размер изображения не должен превышать 1 Мбайт'
            )
        )
    else:
        return image


def validate_not_empty(value):
    if value == '':
        raise forms.ValidationError(
            'Добавьте, пожалуйста, ингредиенты.',
            params={'value': value},
        )  