import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',       # or your DB host
        user='root',            # your MySQL username
        password='',# your MySQL password
        database='college'   # your DB name
    )

