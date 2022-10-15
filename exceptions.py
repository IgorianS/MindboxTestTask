class CustomerIdTypeError(Exception):
    """Некорректный id покупателя, должен быть целым числом"""


class CustomerIdNegotiveError(Exception):
    """Некорректный id покупателя, не может быть меньше 0"""


class CustomersQuantityTypeError(Exception):
    """Некорректное кол-во покупателей, должено быть целым числом"""


class CustomersQuantityNegotiveError(Exception):
    """Некорректное кол-во покупателей, не может быть меньше 0"""


class FirstIdTypeError(Exception):
    """Некорректный начальный id, должен быть целым числом"""


class FirstIdNegotiveError(Exception):
    """Некорректный начальный id, не может быть меньше 0"""


class NonFunctionError(Exception):
    """Должна быть функция в качестве аргумента"""
