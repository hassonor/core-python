import os
import random
from database import connect


def random_string(length):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for i in range(length))


if __name__ == "__main__":
    conn = connect(os.getenv("DB_NAME"))

    # Check if connection was successful
    if conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SALES(
                ORDER_NUM INT PRIMARY KEY,
                CUST_NAME TEXT,
                PROD_NUMBER TEXT,
                PROD_NAME TEXT,
                QUANTITY INT,
                PRICE REAL,
                DISCOUNT REAL,
                ORDER_TOTAL REAL
            );''')

        sales = []
        for _ in range(6):
            order_num = random.randint(1000, 9999)
            cust_name = random_string(5)
            prod_number = "P" + str(random.randint(100, 999))
            prod_name = random_string(5)
            quantity = random.randint(1, 100)
            price = round(random.uniform(10.0, 100.0), 2)
            discount = round(random.uniform(0.0, 10.0), 2)
            order_total = round(price * quantity * (1 - discount / 100), 2)

            sales.append((order_num, cust_name, prod_number, prod_name, quantity, price, discount, order_total))

        cursor.executemany('''
                   INSERT INTO SALES (ORDER_NUM, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''', sales)
        conn.commit()
        conn.close()
