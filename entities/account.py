class Account:
    account_list = []
    account_idx = 1

    def __init__(self, account_id: int, customer_id: int, balance: float):
        self.account_id = account_id
        self.customer_id = customer_id
        self.balance = balance

    def __str__(self):
        return f"account_info: id = {self.account_id}, customer_id = {self.customer_id}, balance = {self.balance}"
