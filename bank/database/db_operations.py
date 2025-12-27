import psycopg2

DB_NAME = "bank_project"
USER_NAME = "postgres"
DB_PASSWORD = "@Bhim@nyu7980"
DB_HOST = "localhost"
DB_PORT = "5432"



def get_connection():
    return psycopg2.connect(
        dbname = DB_NAME ,
        user = USER_NAME ,
        password = DB_PASSWORD ,
        host = DB_HOST , 
        port = DB_PORT 

)



def execute_query(query , params = None):
    conn = get_connection()
    try: 
        with conn :
            with conn.cursor() as cur:
                cur.execute(query , params )
    finally:
        conn.close()

def fetch_query(query, params=None):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()
    finally:
        conn.close()






























