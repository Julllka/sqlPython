import psycopg2

with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
    cur = conn.cursor()

def create_db(conn):
    cur.execute("""CREATE TABLE IF NOT EXISTS customer(
    customer_id SERIAL PRIMARY KEY, 
    first_name VARCHAR(40) NOT NULL,
    second_name VARCHAR(40) NOT NULL,
    email VARCHAR(15) UNIQUE,
    phone VARCHAR(15) UNIQUE
    );""")
    pass

def add_client(conn, first_name, last_name, email, phone=None):
    cur.execute("""
    INSERT INTO customer(first_name) VALUES('Юлия'),
    INSERT INTO customer(second_name) VALUES('Сазонова'),
    INSERT INTO customer(email) VALUES ('EIRU@MAIL.RU');
    """)
    print(cur.fetchall())
    pass


def add_phone(conn, customer_id, phone):
    cur.execute("""
    INSERT INTO customer(phone) VALUES('79110080689');
    """)
    print(cur.fetchall())

    cur.execute("""
    UPDATE customer SET phone = %s WHERE customer_id = %s; 
    """, ('79110080689', id))
    cur.execute("""
    SELECT * FROM customer;
    """)
    print(cur.fetchall())
    pass

def change_client(conn, customer_id, first_name=None, last_name=None, email=None, phones=None):
    cur.execute("""
    UPDATE customer SET second_name = 'Иванова' WHERE second_name = 'Петрова',
    UPDATE customer SET first_name = 'Александра' WHERE first_name = 'Вероника';
    """)
    pass

def delete_phone(conn, client_id, phone):
    cur.execute("""
    DELETE FROM customer WHERE customer_id = '12' AND phone = '79110080689';""")
    pass

def delete_client(conn, client_id):
    cur.execute("""
    DELETE FROM customer WHERE customer_id = '3';""")
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("""
    SELECT customer_id, first_name, second_name,
    FROM customer, 
    WHERE customer_id = '12';""")

    cur.execute("""
    SELECT first_name, second_name,
    FROM customer, 
    WHERE first_name = 'Валентина' AND second_name = "Вишневская"
    ;""")

    cur.execute("""
    SELECT first_name, second_name, phone
    FROM customer, 
    WHERE phone = '79110090879'
    ;""")
return cur.fetchall()

    pass


conn.close()