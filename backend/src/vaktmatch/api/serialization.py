from decimal import Decimal


def exact(value):
    """Behold eksakte desimaler som JSON-strenger, også i sammensatte resultater."""
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {key: exact(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [exact(item) for item in value]
    return value
