import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Elliottadolphus7@uj'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elliott")

print("All Done")
