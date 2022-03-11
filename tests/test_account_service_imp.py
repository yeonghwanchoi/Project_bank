from exception.exception_collection import *
from service_layer.account_service_imp import AccountServiceImp
from service_layer.customer_service_imp import CustomerServiceImp
from dal_layer.account_dao.account_dao_imp import AccountDAOImp

from entities.customer import Customer
from entities.account import Account

_ = CustomerServiceImp()
test_account_service = AccountServiceImp()
test_account_dao = AccountDAOImp()
test_account_dao.create_account(0, 0)

assert Customer.customer_list[0].account_idx_list == [0, 1]
assert Account.account_list[1].customer_id == 0


# withdraw
def test_withdraw_from_account_by_id():
    Account.account_list[0].balance = 1000
    assert test_account_service.withdraw_from_account_by_id(0, 1000) == 0


def test_catch_negative_balance_withdraw_from_account_by_id_():
    Account.account_list[0].balance = 0
    # assert Account.account_list[0].balance == 0
    try:
        test_account_service.withdraw_from_account_by_id(0, 1000)
        assert False
    except NotEnoughAmount as e:
        assert str(e) == 'Not Enough Amount'


def test_catch_negative_value_withdraw():
    try:
        test_account_service.withdraw_from_account_by_id(0, -100)
        assert False
    except ValueError as e:
        assert str(e) == 'Type again'


# transfer
def test_balance_transfer():
    # assert Account.account_list[0].balance == 0 # balance from
    # assert Account.account_list[1].balance == 0 # balance to
    Account.account_list[0].balance = 100
    test_account_service.transfer_money_between_accounts_by_their_ids(0, 1, 100)

    assert Account.account_list[1].balance == 100


def test_catch_negative_balance_transfer():
    # assert len(Customer.customer_list) == 1
    # assert Account.account_list[0].balance == 0 # balance from
    # assert Account.account_list[1].balance == 100 # balance to
    try:
        test_account_service.transfer_money_between_accounts_by_their_ids(0, 1, 100)
        assert False
    except NotEnoughAmount as e:
        assert str(e) == 'Not Enough Amount'


def test_catch_negative_value_transfer():
    # assert len(Account.account_list) == 2
    # assert Account.account_list[0].balance == 0
    # assert Account.account_list[1].balance == 100
    try:
        test_account_service.transfer_money_between_accounts_by_their_ids(0, 1, -100)
        assert False
    except ValueError as e:
        assert str(e) == 'Type again'
