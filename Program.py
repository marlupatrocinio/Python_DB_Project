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
    
conn.set_session(autocommit=True) #each action is commited without having to call conn.commit() after each command

try: #create database
    cur.execute("CREATE DATABASE myfirstdb")
except psycopg2.Error as e:
    print(e)
    
try:
    conn.close()
except psycopg2.Error as e:
    print(e)

try:
    conn = psycopg2.connect("host=localhost dbname=myfirstdb user=postgres password=123456")
except psycopg2.Error as e:
    print("I am unable to connect to the database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("I am unable to get cursor")
    print(e)
    
conn.set_session(autocommit=True)

try: #create the table
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int PRIMARY KEY, name varchar(45), \
                age int, gender varchar(1), subject varchar(10));")
except psycopg2.Error as e:
    print("Error creating the table")
    print(e)
    
try: #insert data
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (1, "Joao", 23, "M", "Python"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: #insert data
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (2, "Maria", 19, "F", "Java"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
#validate the data insertion into the table students

try:
    cur.execute("SELECT * FROM students;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

cur.close()
conn.close()