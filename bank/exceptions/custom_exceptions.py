class InsufficientBalance(Exception):
    def __init__(self, message, balance, attempted):
        super().__init__(message)
        self.balance = balance
        self.attempted = attempted
