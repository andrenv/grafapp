import mysql.connector
import datetime 
import time

dbName = "mydatabase"
tableName = "testtable"

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="example",
)
cursor = db.cursor()
try: # Add if not exist
    cursor.execute("CREATE DATABASE " + dbName)
except Exception as ex:
    print(ex)

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="example",
  database=dbName
)
cursor = db.cursor()

try: # Drop if exist
    cursor.execute("DROP TABLE " + tableName)
except Exception as ex:
    print(ex)

cursor.execute("CREATE TABLE "+ tableName + " (id INT AUTO_INCREMENT PRIMARY KEY, metric VARCHAR(3), time TIMESTAMP, value FLOAT)")
value = 0
sql = "INSERT INTO " + tableName + " (metric, time, value) VALUES (%s, %s, %s)"
while True:
    val = ("bar", datetime.datetime.now(), value)
    cursor.execute(sql, val)
    db.commit()
    value = value + 1
    if value == 10:
        value = 0
    time.sleep(1.0)
