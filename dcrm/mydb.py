import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'password123',
    dbname  = 'postgres'
)

conn.autocommit = True

cursorObject = conn.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")