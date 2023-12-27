import psycopg2

try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123456")
except psycopg2.Error as e:
    print("I am unable to connect to the database")
    print(e)    
    
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("I am unable to get cursor")
    print(e)