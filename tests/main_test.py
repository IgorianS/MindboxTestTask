from main import *
import pytest


def test_customer_group_from_customer_id():
    assert customer_group_from_customer_id(0) == 0
    assert customer_group_from_customer_id(1) == 1
    assert customer_group_from_customer_id(10) == 1
    assert customer_group_from_customer_id(11) == 2
    assert customer_group_from_customer_id(123) == 6

    with pytest.raises(CustomerIdNegotiveError) as error:
        customer_group_from_customer_id(-1)
    assert 'Некорректный id покупателя, не может быть меньше 0' == error.value.args[0]

    with pytest.raises(CustomerIdTypeError) as error:
        customer_group_from_customer_id('1')
    assert 'Некорректный id покупателя, должен быть целым числом' == error.value.args[0]

    with pytest.raises(CustomerIdTypeError) as error:
        customer_group_from_customer_id(1.0)
    assert 'Некорректный id покупателя, должен быть целым числом' == error.value.args[0]


def test_customer_group_from_customer_id_optimized():
    assert customer_group_from_customer_id(0) == 0
    assert customer_group_from_customer_id(1) == 1
    assert customer_group_from_customer_id(10) == 1
    assert customer_group_from_customer_id(11) == 2
    assert customer_group_from_customer_id(123) == 6

    with pytest.raises(CustomerIdNegotiveError) as error:
        customer_group_from_customer_id(-1)
    assert 'Некорректный id покупателя, не может быть меньше 0' == error.value.args[0]

    with pytest.raises(CustomerIdTypeError) as error:
        customer_group_from_customer_id('1')
    assert 'Некорректный id покупателя, должен быть целым числом' == error.value.args[0]

    with pytest.raises(CustomerIdTypeError) as error:
        customer_group_from_customer_id(1.0)
    assert 'Некорректный id покупателя, должен быть целым числом' == error.value.args[0]


def test_count_customers_by_groups():
    with pytest.raises(CustomersQuantityNegotiveError) as error:
        count_customers_by_groups(-1)
    assert 'Некорректное кол-во покупателей, не может быть меньше 0' == error.value.args[0]

    with pytest.raises(CustomersQuantityTypeError) as error:
        count_customers_by_groups('1')
    assert 'Некорректное кол-во покупателей, должено быть целым числом' == error.value.args[0]

    with pytest.raises(CustomersQuantityTypeError) as error:
        count_customers_by_groups(1.0)
    assert 'Некорректное кол-во покупателей, должено быть целым числом' == error.value.args[0]

    with pytest.raises(FirstIdNegotiveError) as error:
        count_customers_by_groups(1, -1)
    assert 'Некорректный начальный id, не может быть меньше 0' == error.value.args[0]

    with pytest.raises(FirstIdTypeError) as error:
        count_customers_by_groups(1, '1')
    assert 'Некорректный начальный id, должен быть целым числом' == error.value.args[0]

    with pytest.raises(FirstIdTypeError) as error:
        count_customers_by_groups(1, 1.0)
    assert 'Некорректный начальный id, должен быть целым числом' == error.value.args[0]

    with pytest.raises(NonFunctionError) as error:
        count_customers_by_groups(1, 0, 1)
    assert 'Должна быть функция в качестве аргумента' == error.value.args[0]


def test_print_assessment_result():
    pass


if __name__ == '__main__':
    pytest.main()
