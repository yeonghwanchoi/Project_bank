from exception.exception_collection import *
from entities.customer import Customer
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.account import Account

test_customer = CustomerDAOImp()


def test_create_customer():
    assert test_customer.create_customer('yeonghwan', 'choi')


def test_catch_long_name():
    try:
        test_customer.create_customer('asdfdsasdadsadsadafdsafdsa', 'asdsadsdsafdsafdsafdsafdsafadsad')
        assert False
    except TooLongName as e:
        assert str(e) == 'Too Long Name less than 20 characters'


def test_catch_non_char_name():
    try:
        test_customer.create_customer('11111', 'asdsadsadsad')
        assert False
    except InValidName as e:
        assert str(e) == 'InValid Name'

    try:
        test_customer.create_customer('@!#$', 'asdsadsadsad')
        assert False
    except InValidName as e:
        assert str(e) == 'InValid Name'


def test_catch_unique_id():
    result = test_customer.create_customer('asd', 'asdf')
    result2 = test_customer.create_customer('asdq', 'ASXCzxc')
    assert result.customer_id != result2.customer_id


def test_delete_customer_by_id():
    test_customer.create_customer('test', 'test')
    test_customer.delete_customer_by_id(1)
    assert Customer.customer_list[1] is None


def test_delete_customer_by_id_no_id():
    id = len(Customer.customer_list) + 1

    try:
        test_customer.delete_customer_by_id(id)
        assert False
    except NotFound as e:
        assert str(e) == 'Not Found'


def test_delete_customer_by_id_None_value():
    id = 0
    Customer.customer_list[id] = None
    try:
        test_customer.delete_customer_by_id(id)
        assert False
    except NotFound as e:
        assert str(e) == 'Not Found'
