from abc import ABC, abstractmethod
from entities.customer import Customer


class CustomerDAOInterface(ABC):
    #
    @abstractmethod
    def customer_information(self, customer_id: int)-> Customer:
        pass

    @abstractmethod
    def create_customer(self, first_name: str, last_name: str) -> Customer:
        pass

    @abstractmethod
    def delete_customer_by_id(self, id: int) -> bool:
        pass

