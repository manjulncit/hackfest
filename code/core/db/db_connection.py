import mysql.connector
from mysql.connector import errorcode

from dotenv import load_dotenv

load_dotenv()

import os

class DBConnection():

	def init_conn(self):

		conn = None
		cursor = None

		host = os.environ["DB_HOST"]
		user = os.environ["DB_USER"]
		password = os.environ["DB_PASSWORD"]
		database = os.environ["DB_NAME"]

		try:
			conn = mysql.connector.connect(user=user, password=password,host=host,database=database) 
			cursor = conn.cursor()
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
		return conn, cursor
