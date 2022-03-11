from entities.account import Account
from service_layer.customer_service_imp import CustomerServiceImp
from entities.customer import Customer
from exception.exception_collection import *

customer_service = CustomerServiceImp()

a, b, c = Account(0, 0, 0), Account(1, 0, 0), Account(2, 0, 0)

Account.account_list = [a.account_id, b.account_id, c.account_id]


def test_get_all_accounts_for_user():
    Customer.customer_list[0].account_idx_list = [0, 1, 2]

    result = customer_service.get_all_accounts_for_user(0)

    assert result == Account.account_list


def test_get_all_accounts_for_user_no_accounts_list():
    try:
        Customer.customer_list[0].account_idx_list = []
        customer_service.get_all_accounts_for_user(0)

    except NotFound as e:
        assert str(e) == 'No accounts'
