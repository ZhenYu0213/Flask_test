# Connect MySQL
import json
from json import JSONEncoder
import mysql.connector
import flask

# constructor
myDB = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "changeisgood",
  database = "webchatroom",
)
cursor=myDB.cursor()

# methods
def GetUserInfo():
  if(myDB.is_connected()):
    cursor.execute("SELECT UserAccount,UserPassword FROM userinfo;")
    rows=cursor.fetchall()
    return rows