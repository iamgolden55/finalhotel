import mysql.connector

host = "localhost"
user = "root"
passwd = "alpha12345"
database = "JOB_DB"

try:
    conn = mysql.connector.connect(host=host, user=user, password=passwd, database=database)
    print("Connection to database successful")
    dbcursor = conn.cursor()
except mysql.connector.Error as e:
    print("Connection to database failed")

    conn.close()