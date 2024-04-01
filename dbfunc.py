import mysql.connector

def fetch_data(query):
    host = "localhost"
    user = "root"
    passwd = "alpha12345"
    db_base = "JOB_DB"
    
    try:
        conn = mysql.connector.connect(host=host, user=user, password=passwd, database=db_base)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except mysql.connector.Error as e:
        print("Error fetching data:", e)
        return None
    finally:
        if conn.is_connected():
            conn.close()