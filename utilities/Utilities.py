from entities.account import Account
from entities.customer import Customer
from psycopg import OperationalError, connect
import os


def get_customer_info(customer_obj) -> Customer:
    if len(customer_obj.account_idx_list) == 0:
        account_list_info = "you don't have any account"
    else:
        account_list_info = list(map(lambda x: f"account id = {x} ", customer_obj.account_idx_list))

    customer_response_dict = {
        "customerId": customer_obj.customer_id,
        "firstName": customer_obj.customer_first_name,
        "lastName": customer_obj.customer_last_name,
        "account_idx_list": account_list_info
    }
    return customer_response_dict


def get_account_info(account_obj) -> Account:
    account_response_dict = {
        "accountId": account_obj.account_id,
        "balance": account_obj.balance,
        "customer_id": account_obj.customer_id,
    }
    return account_response_dict


def get_all_account_info(customer_id) -> list:
    account_list = customer_id.account_idx_list
    account_response_dict = {f" account_id {i} balance ": Account.account_list[i].balance for i in account_list}
    return account_response_dict


def create_connection():
    try:
        conn = connect(

            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        print(e)


connection = create_connection()

print(connection)
