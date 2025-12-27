
class Account:
    def __init__(self, customer_id, account_type, balance=0):
        self.customer_id = customer_id      # FK to customer
        self.account_type = account_type
        self.balance = balance
