from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from service_layer.customer_service_imp import CustomerServiceImp
from service_layer.account_service_imp import AccountServiceImp
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp

from exception.exception_collection import *
from utilities.Utilities import *

from flask import Flask, request, jsonify

app: Flask = Flask(__name__)

CSI = CustomerServiceImp()
CDI = CustomerDAOImp()
ASI = AccountServiceImp()
ADI = AccountDAOImp()

Customer.customer_list[0].account_idx_list = [0]
Account.account_list[0].balance = 1000
CDI.create_customer('test', 'test')
ADI.create_account(1, 0)

assert Customer.customer_list[0].account_idx_list == [0]
assert Account.account_list[0].balance == 1000

assert Customer.customer_list[1].customer_id == 1
assert Account.account_list[1].balance == 0


# As a customer, I can start a business relationship with the bank so I can store my money securely(create_customer)
@app.route("/create_customer", methods=["POST"])
def create_customer():
    try:
        request_content = request.get_json()
        new_customer = CDI.create_customer(request_content["first_name"], request_content["last_name"])
        result = jsonify(get_customer_info(new_customer))
        return result, 200
    except InValidName as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except TooLongName as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


# As a customer, I can create a new bank account with a starting balance so I have somewhere to store my money
# (create_account)
@app.route("/create_account", methods=["POST"])
def create_account():
    try:
        request_content = request.get_json()
        new_customer = ADI.create_account(int(request_content["customer_id"]), float(request_content["amount"]))
        return jsonify(get_account_info(new_customer))
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except NotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


# As a customer, I can view the balance of a specific account so I can check my finances
# (get_account_by_id)
@app.route("/get_account_by_id/<account_id>", methods=["GET"])
def get_account_by_id(account_id: int):
    try:
        tmp_account = ADI.get_account_by_id(int(account_id))
        return jsonify(get_account_info(tmp_account))
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except NotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


# as a customer, I can view the balance of all my accounts so I know exactly how much money I have
# (get_all_accounts_for_user)
@app.route("/get_all_accounts_for_user/<customer_id>", methods=["GET"])
def get_all_accounts_for_user(customer_id: int):
    try:
        tmp_list = CSI.get_all_accounts_for_user(int(customer_id))
        account_response_dict = {f" account_id {i} balance ": float(Account.account_list[i].balance) for i in tmp_list}
        return jsonify(account_response_dict)
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except NotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


# As a customer, I can make a withdrawal from a specific account so I can have access to my money
# (withdraw_from_account_by_id)
@app.route("/withdraw_from_account_by_id/<account_id>/<amount>", methods=["GET"])
def withdraw_from_account_by_id(account_id: int, amount: float):
    try:
        tmp_balance = ASI.withdraw_from_account_by_id(int(account_id), float(amount))
        account_response_dict = {"withdraw amount": float(amount), "remaining balance": tmp_balance}
        return jsonify(account_response_dict)
    except NotEnoughAmount as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)

    # As a customer, I can make a deposit to a specific account so I can store my money for safe keeping


# (deposit_into_account_by_id)
@app.route("/deposit_into_account_by_id/<account_id>/<amount>", methods=["GET"])
def deposit_into_account_by_id(account_id: int, amount: float):
    try:
        tmp_balance = ASI.deposit_into_account_by_id(int(account_id), float(amount))
        account_response_dict = {"deposit amount": float(amount), "remaining balance": tmp_balance}
        return jsonify(account_response_dict)
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


# As a customer, I can transfer money between accounts so I can consolidate my money
# (transfer_money_between_accounts_by_their_ids)
@app.route("/transfer_money_between_accounts_by_their_ids/<account_id_from>/<account_id_to>/<amount>", methods=["GET"])
def transfer_money_between_accounts_by_their_ids(account_id_from: int, account_id_to: int, amount: float):
    try:
        tmp_balance_from, tmp_balance_to = ASI.transfer_money_between_accounts_by_their_ids(int(account_id_from),
                                                                                            int(account_id_to),
                                                                                            float(amount))
        account_response_dict = {"transfer amount": float(amount),
                                 f"from account{account_id_from} remaining balance": tmp_balance_from,
                                 f"to account{account_id_to} remaining balance": tmp_balance_to}
        return jsonify(account_response_dict)
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except NotEnoughAmount as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


# As a customer, I can close any of my bank accounts so that it is easier to remember where my money resides
# (delete_account_by_id)
@app.route("/delete_account_by_id/<account_id>", methods=["GET"])
def delete_account_by_id(account_id: int, ):
    try:
        ADI.delete_account_by_id(int(account_id))
        account_response_dict = f'account{account_id} is deleted'
        return jsonify(account_response_dict)
    except NotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except IndexError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


# As a customer, I can end my relationship with the bank when it is no longer needed
# (delete_customer_by_id)
@app.route("/delete_customer_by_id/<customer_id>", methods=["GET"])
def delete_customer_by_id(customer_id: int, ):
    try:
        CDI.delete_customer_by_id(int(customer_id))
        account_response_dict = f'customer{customer_id} is deleted'
        return jsonify(account_response_dict)
    except ValueError as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)
    except NotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message)


if __name__ == '__main__':
    app.run()
