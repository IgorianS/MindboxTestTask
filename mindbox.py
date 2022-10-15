from exceptions import *
from collections import Counter
from statistics import variance, stdev
from time import time


def customer_group_from_customer_id(customer_id: int) -> int:
    """
    Базовая функция распределения покупателя по группам
    :param customer_id: id покупателя
    :return: номер группы
    """
    if not isinstance(customer_id, int):
        raise CustomerIdTypeError('Некорректный id покупателя, должен быть целым числом')
    if customer_id < 0:
        raise CustomerIdNegotiveError('Некорректный id покупателя, не может быть меньше 0')

    customer_group = 0
    while customer_id != 0:
        customer_id, last_digit = divmod(customer_id, 10)
        customer_group += last_digit

    return customer_group


def customer_group_from_customer_id_optimized(customer_id: int, n_groups: int = 10) -> int:
    """
    Оптимизированная функция распределения покупателя по группам.
    Можно указать, на сколько групп необходимо распределять покупателей
    :param customer_id: id покупателя
    :param n_groups: кол-во групп для разбиения
    :return: номер группы
    """
    if not isinstance(customer_id, int):
        raise CustomerIdTypeError('Некорректный id покупателя, должен быть целым числом')
    if customer_id < 0:
        raise CustomerIdNegotiveError('Некорректный id покупателя, не может быть меньше 0')

    return customer_id % n_groups


def count_customers_by_groups(n_customers: int, n_first_id: int = 0,
                              distribution_function=customer_group_from_customer_id) -> Counter:
    """
    Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная.
    Объединяет обе требуемые функции. Позволяет выбирать функцию распределения.
    :param n_customers: кол-во клиентов
    :param n_first_id: первый ID в последовательности, по умолчанию 0
    :param distribution_function: функция распределения, по умолчанию базовая
    :return: словарь групп и кол-ва покупателей в них
    """
    if not isinstance(n_customers, int):
        raise CustomersQuantityTypeError('Некорректное кол-во покупателей, должено быть целым числом')
    if n_customers < 0:
        raise CustomersQuantityNegotiveError('Некорректное кол-во покупателей, не может быть меньше 0')
    if not isinstance(n_first_id, int):
        raise FirstIdTypeError('Некорректный начальный id, должен быть целым числом')
    if n_first_id < 0:
        raise FirstIdNegotiveError('Некорректный начальный id, не может быть меньше 0')
    if not callable(distribution_function):
        raise NonFunctionError('Должна быть функция в качестве аргумента')

    groups = Counter()
    for customer_id in range(n_first_id, n_customers + n_first_id + 1):
        groups[distribution_function(customer_id)] += 1

    return groups


def print_assessment_result(n_customers: int, n_first_id: int, distribution_function) -> None:
    """
    Функция вывода в консоль результатов оценки работы разных функций распределения покупателей по группам.
    :param n_customers: кол-во клиентов
    :param n_first_id: первый ID в последовательности, по умолчанию 0
    :param distribution_function: функция распределения
    :return:
    """
    start = time()
    groups = count_customers_by_groups(n_customers, n_first_id, distribution_function)
    stop = time()
    print(f"Результат работы функции {distribution_function.__name__}")
    print(f"Кол-во покупателей по группам (номер группы, кол-во покупателей):")
    print(*groups.items())
    print(f"Дисперсия: {variance(groups.values()):.2f}, стандарное отклонение: {stdev(groups.values()):.2f}")
    print(f'Время работы {(stop - start):.4f} сек')


if __name__ == '__main__':
    N_CUSTOMER = 741256
    N_FIRST_ID = 0

    try:
        print_assessment_result(N_CUSTOMER, N_FIRST_ID, customer_group_from_customer_id)
        print()
        print_assessment_result(N_CUSTOMER, N_FIRST_ID, customer_group_from_customer_id_optimized)

    except CustomerIdNegotiveError:
        print("Некорректный id покупателя, не может быть меньше 0")
    except CustomerIdTypeError:
        print("Некорректный id покупателя, должен быть целым числом")
    except CustomersQuantityNegotiveError:
        print("Некорректное кол-во покупателей, не можно быть меньше 0")
    except CustomersQuantityTypeError:
        print("Некорректное кол-во покупателей, должено быть целым числом")
    except FirstIdNegotiveError:
        print("Некорректный начальный id, не может быть меньше 0")
    except FirstIdTypeError:
        print("Некорректный начальный id, должен быть целым числом")
    except NonFunctionError:
        print("Должна быть функция в качестве аргумента")
