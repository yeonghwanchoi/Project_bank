from abc import ABC, abstractmethod
from entities.account import Account


class AccountServiceInterface(ABC):

    @abstractmethod
    def withdraw_from_account_by_id(self, account_id: int, amount: float) -> float:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, account_id: int, amount: float) -> float:
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, account_id_from: int, account_id_to: int, amount: float):
        pass


