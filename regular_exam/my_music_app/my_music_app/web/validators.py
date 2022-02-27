from django.core.exceptions import ValidationError

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validator(value):
    for ch in value:
        if ch.isalpha() or ch.isnumeric() or ch == '_':
            continue
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)

