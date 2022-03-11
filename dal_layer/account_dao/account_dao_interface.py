from abc import ABC, abstractmethod
from entities.account import Account


class AccountDAOInterface(ABC):

    @abstractmethod
    def get_account_by_id(self, account_id : int) -> Account:
        pass

    @abstractmethod
    def create_account(self, customer_id: int) -> Account:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass