from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer import Customer
from exception.exception_collection import *
from utilities.Utilities import *
import re


class CustomerDAOImp(CustomerDAOInterface):

    def __init__(self):
        tmp = Customer('yeonghwan', 'choi', 0)
        # tmp.account_idx_list = [0,1,2,3]
        if len(Customer.customer_list) == 0:
            Customer.customer_list.append(tmp)

    def create_customer(self, first_name: str, last_name: str) -> Customer:
        idx = Customer.customer_idx
        if type(first_name) and type(last_name) != str:
            raise InValidName('InValid Name')
        elif re.search(r'[^a-zA-Z]', first_name + last_name) is not None:
            raise InValidName('InValid Name')
        elif len(first_name) > 20 and len(last_name) > 20:
            raise TooLongName('Too Long Name less than 20 characters')
        else:
            tmp_customer = Customer(first_name, last_name, idx)
            Customer.customer_list.append(tmp_customer)
            Customer.customer_idx += 1
            return tmp_customer

    def customer_information(self, customer_id: int) -> Customer:
        if type(customer_id) != int:
            raise ValueError('type again')
        elif customer_id + 1 > len(Customer.customer_list):
            raise NotFound('Not Found')
        else:
            return get_customer_info(Customer.customer_list[customer_id])

    def delete_customer_by_id(self, customer_id: int) -> bool:
        if type(customer_id) != int:
            raise ValueError('type again')
        elif customer_id + 1 > len(Customer.customer_list):
            raise NotFound('Not Found')
        elif Customer.customer_list[customer_id] is None:
            raise NotFound("Not Found")
        else:
            Customer.customer_list[customer_id] = None
            for i in Customer.account_idx_list:
                Account.account_list[i] = None
            return True

# CustomerDAOImp()
# print(get_customer_info(Customer.customer_list[0]))
