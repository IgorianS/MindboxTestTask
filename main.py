from collections import Counter
from statistics import variance, stdev
from time import time


class ExceptionCustomerId(Exception):
    """Некорректный id покупателя, не может быть меньше 0."""


class ExceptionCustomersQuantity(Exception):
    """Некорректное кол-во покупателей, не может быть меньше 0."""


class ExceptionFirstId(Exception):
    """Некорректный начальный id, не может быть меньше 0."""


def customer_group_from_customer_id(customer_id: int) -> int:
    """
    Базовая функция распределения покупателя по группам
    :param customer_id: id покупателя
    :return: номер группы
    """
    if customer_id < 0:
        raise ExceptionCustomerId()

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
    if customer_id < 0:
        raise ExceptionCustomerId()

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
    if n_customers < 0:
        raise ExceptionCustomersQuantity()
    if n_first_id < 0:
        raise ExceptionFirstId()

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
    print(f"Кол-во покупателей по группам (номер группы, кол-во покупателей):")
    print(*groups.items())
    print(f"Дисперсия: {variance(groups.values()):.2f}, стандарное отклонение: {stdev(groups.values()):.2f}")
    print(f'Время работы {(stop - start):.4f} сек')


if __name__ == '__main__':
    N_CUSTOMER = 741256
    N_FIRST_ID = 0

    try:
        print(f"Результат работы базовой функции")
        print_assessment_result(N_CUSTOMER, N_FIRST_ID, customer_group_from_customer_id)
        print()

        print(f"Результат работы оптимизированной функции")
        print_assessment_result(N_CUSTOMER, N_FIRST_ID, customer_group_from_customer_id_optimized)

    except ExceptionCustomerId:
        print("Некорректный id покупателя, не может быть меньше 0.")
    except ExceptionCustomersQuantity:
        print("Некорректное кол-во покупателей, не может быть меньше 0.")
    except ExceptionFirstId:
        print("Некорректный начальный id, не может быть меньше 0.")
