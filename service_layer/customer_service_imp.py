from service_layer.customer_service_interface import CustomerServiceInterface
from exception.exception_collection import *
from entities.customer import Customer

import re


class CustomerServiceImp(CustomerServiceInterface):
    def __init__(self):
        self.tmp = Customer('yeonghwan', 'choi', 0)
        if len(Customer.customer_list) == 0:
            Customer.customer_list.append(self.tmp)

    def get_all_accounts_for_user(self, customer_id: int) -> list:

        if type(customer_id) != int:
            raise ValueError('type again')
        elif len(Customer.customer_list) < customer_id + 1:
            raise NotFound('No accounts')
        elif len(Customer.customer_list[customer_id].account_idx_list) == 0:
            raise NotFound('No accounts')
        else:
            tmp_customer = Customer.customer_list[customer_id]
            result_list = [i for i in tmp_customer.account_idx_list]
            return result_list
