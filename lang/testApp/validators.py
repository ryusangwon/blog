from django.core.exceptions import ValidationError

def validate_test(value):
    if ('*' in value):
        raise ValidationError('"*"사용 불가')