from bank.database.db_operations import execute_query, fetch_query
from bank.exceptions.custom_exceptions import InsufficientBalance

class TransactionService:
    
    def create_account(self, account):
        """Insert a new account into DB and return the account_id"""
        result = fetch_query(
            """
            INSERT INTO account (customerid, account_type, balance)
            VALUES (%s, %s, %s)
            RETURNING account_id
            """,
            (account.customer_id, account.account_type, account.balance)
        )
        return result[0][0]

    def deposit(self, account_id, amount, mode):
        execute_query(
            "UPDATE account SET balance = balance + %s WHERE account_id = %s",
            (amount, account_id)
        )
        execute_query(
            """
            INSERT INTO transactions (account_id, transaction_type, transaction_mode, amount)
            VALUES (%s, 'DEPOSIT', %s, %s)
            """,
            (account_id, mode, amount)
        )

    def withdraw(self, account_id, amount, mode):
        balance = fetch_query(
            "SELECT balance FROM account WHERE account_id = %s",
            (account_id,)
        )[0][0]

        if amount > balance:
            raise InsufficientBalance("Insufficient Balance", balance, amount)

        execute_query(
            "UPDATE account SET balance = balance - %s WHERE account_id = %s",
            (amount, account_id)
        )

        execute_query(
            """
            INSERT INTO transactions (account_id, transaction_type, transaction_mode, amount)
            VALUES (%s, 'WITHDRAWAL', %s, %s)
            """,
            (account_id, mode, amount)
        )

    def get_balance(self, account_id):
        result = fetch_query(
            "SELECT balance FROM account WHERE account_id = %s",
            (account_id,)
        )
        if result:
            return float(result[0][0])
        return None
