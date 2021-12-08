from decimal import Decimal


def to_decimal(num: str) -> Decimal:
    """
    transform string into decimal with two places
    example:
      to_decimal('123.4567') -> Decimal('123.45')
    """
    return Decimal(num).quantize(Decimal(10) ** -2)
