from django.core.exceptions import ValidationError


def validate_file_size(image):
    filesize = image.size
    if filesize > 1000000:
        raise ValidationError(
            message=(
                'Максимальный размер изображения не должен превышать  1 Мбайт'
            )
        )
    else:
        return image
