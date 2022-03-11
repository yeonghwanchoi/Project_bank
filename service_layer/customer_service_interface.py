from abc import ABC, abstractmethod



class CustomerServiceInterface(ABC):

    @abstractmethod
    def get_all_accounts_for_user(self, id: int) -> list:
        pass
