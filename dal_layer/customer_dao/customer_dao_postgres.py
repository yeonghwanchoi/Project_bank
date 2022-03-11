from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer import Customer
from exception.exception_collection import *
from utilities.Utilities import *
import re


# class Person:
#     def __init__(self, person_id, first_name, last_name):
#         self.person_id = person_id
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"person_id = {self.person_id}, first_name = {self.first_name}, last_name = {self.last_name}"
#
#
# def create_person_entry(person: Person):
#         # create sql query
#     sql = "insert into persons values(default,%s,%s) returning person_id"
#         # create cursor object to handle our query
#     cursor = connection.cursor()
#         # have cursor object send query to database
#     cursor.execute(sql,(person.first_name, person.last_name))
#         # commit our query
#     connection.commit()
#         # end our function
#         # tuple_info = cursor.fetchone()
#         # new_id = tuple_info[0]
#     new_id = cursor.fetchone()[0]
#     person.person_id = new_id
#     return person
#
# my_person = Person(0,"yeonghwan", "choi") # this is my person object i will pass into the function
# print(create_person_entry(my_person)) # this will print the values off the object that is passed into the database

class CustomerDAOImpPostgres(CustomerDAOInterface):

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
            return True
