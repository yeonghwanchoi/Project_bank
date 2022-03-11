class Customer:
    customer_list = []
    customer_idx = 1

    def __init__(self, first_name: str, last_name: str, customer_id: int):
        self.customer_id = customer_id
        self.customer_first_name = first_name
        self.customer_last_name = last_name
        self.account_idx_list = []

    def __str__(self):
        return f"customer_info: id = {self.customer_id}, name = {self.customer_first_name + ' ' + self.customer_last_name}"
