from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from service_layer.account_service_imp import AccountServiceImp
from service_layer.customer_service_imp import CustomerServiceImp

from exception.exception_collection import *

from entities.account import Account
from entities.customer import Customer

_ = CustomerServiceImp()
test_account_service = AccountServiceImp()
test_account_dao = AccountDAOImp()
test_account_dao.create_account(0, 0)

# assert Customer.customer_list[0].account_idx_list == [0, 1]
# assert Account.account_list[1].customer_id == 0

# We have one customer obj that has customer_id = 0, two account with 0, 1

def test_get_account_by_id():
    id = 1
    # assert len(Account.account_list) == 2  # test account id:0 balance: 0
    assert test_account_dao.get_account_by_id(id).account_id == id


def test_get_account_by_id_no_id():
    try:
        assert len(Account.account_list) == 2
        id = 100
        test_account_dao.get_account_by_id(id)
        assert False

    except NotFound as e:
        assert str(e) == 'Account Not Found'


# create
def test_create_account():
    test_account_dao.create_account(0, 100)
    assert Account.account_list[2].balance == 100


def test_catch_create_account_wrong_input_values():
    try:
        test_account_dao.create_account(0, - 100)
        assert False
    except ValueError as e:
        assert str(e) == 'Type again'


def test_catch_create_account_wrong_input_id():
    id = len(Customer.customer_list) + 1
    assert len(Customer.customer_list) == 1

    try:
        test_account_dao.create_account(id, 0)
        assert False
    except NotFound as e:
        assert str(e) == 'Not Found'


# delete
def test_delete_account_by_id():
    id = 1
    # assert Account.account_list[1].customer_id == 0
    # assert Customer.customer_list[0].account_idx_list == [0, 1]

    test_account_dao.delete_account_by_id(id)
    assert Account.account_list[id] is None
    # assert Customer.customer_list[0].account_idx_list == [0]
    # assert len(Account.account_list) == 2


def test_catch_delete_account_by_no_id():
    id = 100

    try:
        test_account_dao.delete_account_by_id(id)
        assert False
    except NotFound as e:
        assert str(e) == 'Not found'


def test_catch_delete_account_by_id_None_account():
    id = 1

    # assert len(Account.account_list) == 3
    # Account.account_list[1] = None

    try:
        test_account_dao.delete_account_by_id(id)
        assert False
    except NotFound as e:
        assert str(e) == 'Not found'


def test_catch_delete_account_by_id_no_account_idx():
    id = 2

    test_account_dao.create_account(0, 100)

    # assert Customer.customer_list[0].account_idx_list == [0, 2, 3]

    Customer.customer_list[0].account_idx_list.remove(2)
    try:
        test_account_dao.delete_account_by_id(id)
        assert False
    except IndexError as e:
        assert str(e) == 'Index is not found'
