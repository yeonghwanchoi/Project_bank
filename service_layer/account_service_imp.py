from service_layer.account_service_interface import AccountServiceInterface
from exception.exception_collection import *
from entities.account import Account
from entities.customer import Customer


class AccountServiceImp(AccountServiceInterface):

    def __init__(self):
        self.tmp = Account(0, 0, 0)
        if len(Account.account_list) == 0:
            Account.account_list.append(self.tmp)
            Customer.customer_list[0].account_idx_list.append(0)

    def withdraw_from_account_by_id(self, account_id: int, amount: float) -> float:

        if type(amount) != int and type(amount) != float:
            raise ValueError('Type again')
        elif amount <= 0:
            raise ValueError('Type again')
        elif Account.account_list[account_id].balance - amount < 0:
            raise NotEnoughAmount('Not Enough Amount')
        else:
            tmp_balance = Account.account_list[account_id].balance
            tmp_balance -= amount
            return tmp_balance

    def deposit_into_account_by_id(self, account_id: int, amount: float) -> float:

        if type(account_id) != int and type(amount) != float and type(amount) != int:
            raise ValueError('Type again')
        elif amount <= 0:
            raise ValueError('Type again')
        else:
            tmp_balance = Account.account_list[account_id].balance
            tmp_balance += amount
            return tmp_balance

    def transfer_money_between_accounts_by_their_ids(self, account_id_from: int, account_id_to: int, amount: float):

        if type(account_id_to) != int and type(account_id_from) != int and type(amount) != float and type(
                amount) != int:
            raise ValueError('Type again')
        elif amount <= 0:
            raise ValueError('Type again')
        elif Account.account_list[account_id_from].balance < amount:
            raise NotEnoughAmount('Not Enough Amount')
        else:

            Account.account_list[account_id_from].balance -= amount
            Account.account_list[account_id_to].balance += amount

            balance_from = Account.account_list[account_id_from].balance
            balance_to = Account.account_list[account_id_to].balance
            return balance_from, balance_to
