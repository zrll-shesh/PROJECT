from faker import Faker
import random
import mysql.connector
from datetime import datetime, timedelta

fake = Faker()

# Connect ke MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123nazril16#",
    database="ecommerce_db",
    port=3306
)
cursor = conn.cursor()

# Hapus data lama agar tidak duplicate
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")  # matikan sementara FK
cursor.execute("TRUNCATE TABLE transactions")
cursor.execute("TRUNCATE TABLE customers")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")  # aktifkan kembali FK
conn.commit()

# Generate 10.000 customers
for i in range(1, 10001):
    name = fake.name()
    gender = random.choice(['M','F'])
    join_date = fake.date_between(start_date='-3y', end_date='today')
    region = fake.state()
    device = random.choice(['Mobile','Desktop','Tablet'])
    
    cursor.execute("""
        INSERT INTO customers (customer_id, name, gender, join_date, region, device)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (i, name, gender, join_date, region, device))

conn.commit()

for i in range(1, 20001):
    customer_id = random.randint(1, 10000)
    transaction_date = fake.date_between(start_date='-2y', end_date='today')
    amount = round(random.uniform(10, 1000),2)
    payment_method = random.choice(['Credit Card','Debit Card','E-Wallet','Cash'])
    
    cursor.execute("""
        INSERT INTO transactions (transaction_id, customer_id, transaction_date, amount, payment_method)
        VALUES (%s,%s,%s,%s,%s)
    """, (i, customer_id, transaction_date, amount, payment_method))

conn.commit()
cursor.close()
conn.close()
