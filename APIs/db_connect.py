import mysql.connector

def db_connect():
	mydb = mysql.connector.connect(
		host="localhost",
		user="pd",
		passwd="pawan123",
		database="etaal")
	mycursor = mydb.cursor()
	return mycursor