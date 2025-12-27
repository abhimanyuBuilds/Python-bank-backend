from bank.database.db_operations import fetch_query

class CustomerService:

    def create_customer(self, customer):
        # 1️⃣ FIRST check if customer already exists
        existing = fetch_query(
            "SELECT customerid FROM customer WHERE contact = %s",
            (customer.contact,)
        )

        if existing:
            # Customer already exists → return existing ID
            return existing[0][0]

        # 2️⃣ Insert ONLY if not exists
        result = fetch_query(
            """
            INSERT INTO customer
            (name, address, contact, username, password, email)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING customerid
            """,
            (
                customer.name,
                customer.address,
                customer.contact,
                customer.username,
                customer.password,
                customer.email
            )
        )

        return result[0][0]
