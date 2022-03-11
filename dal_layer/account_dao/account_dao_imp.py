from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from exception.exception_collection import *
from entities.account import Account
from entities.customer import Customer


class AccountDAOImp(AccountDAOInterface):

    # account_idx = 1
    def __init__(self):
        self.tmp = Account(0, 0, 0)
        if len(Account.account_list) == 0:
            Account.account_list.append(self.tmp)

    def create_account(self, customer_id: int, amount) -> Account:
        if type(customer_id) != int:
            raise ValueError('Type again')
        elif customer_id + 1 > len(Customer.customer_list):
            raise NotFound('Not Found')
        elif type(amount) != int and type(amount) != float:
            raise ValueError('Type again')
        elif amount < 0:
            raise ValueError('Type again')
        else:
            idx = Account.account_idx

            new_account = Account(idx, customer_id, amount)
            new_account.customer_id = customer_id

            Account.account_list.append(new_account)
            Customer.customer_list[customer_id].account_idx_list.append(idx)

            Account.account_idx += 1
            return Account.account_list[Account.account_idx - 1]

    def delete_account_by_id(self, account_id: int) -> bool:
        if type(account_id) != int:
            raise ValueError('Type again')
        elif account_id + 1 > len(Account.account_list):
            raise NotFound('Not found')
        elif Account.account_list[account_id] is None:
            raise NotFound('Not found')
        else:
            tmp_account = Account.account_list[account_id]
            tmp_customer_id = tmp_account.customer_id
            tmp_customer = Customer.customer_list[tmp_customer_id]

            if account_id not in tmp_customer.account_idx_list:
                raise IndexError('Index is not found')
            else:
                Account.account_list[account_id] = None
                tmp_customer.account_idx_list.remove(account_id)
                return True

    def get_account_by_id(self, account_id: int) -> Account:
        tmp_list = Account.account_list
        if type(account_id) != int:
            raise ValueError('type again')
        elif account_id + 1 > len(tmp_list):
            raise NotFound('Account Not Found')
        elif tmp_list[account_id] is None:
            raise NotFound('Account Not Found')
        else:
            return Account.account_list[account_id]
