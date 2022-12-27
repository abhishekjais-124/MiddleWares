from django.core.exceptions import ValidationError

def validate_name_starting_with_a(value):
    if not value or value[0] not in ['a','A']:
        raise ValidationError(f"{value} is not starting with character a or A")