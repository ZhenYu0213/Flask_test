# Connect MySQL
import json
from json import JSONEncoder
import mysql.connector
import flask

# constructor
myDB = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "jack040520",
  database = "webdatabase",
)
cursor=myDB.cursor(dictionary=True)

# methods
def GetUserInfo():
  if(myDB.is_connected()):
    cursor.execute("SELECT userAccount,userPassword FROM userinfo;")
    rows=cursor.fetchall()
    return rows