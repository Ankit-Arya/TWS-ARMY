import mysql.connector
from mysql.connector import errorcode

try:
    dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'Ankit.1993'

        )
    print('All Okay')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)