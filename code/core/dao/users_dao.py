from core.db.db_connection import DBConnection

class UserDAO():

	def __init__(self):
		self.db_conn = DBConnection()

	def get_all_users(self):
		conn,cursor = self.db_conn.init_conn()

		resp = {}
		res = None
		status = False
		message = ""
		try:
			query = "SELECT * FROM users123;"

			cursor.execute(query)

			res = cursor.fetchall()
			status = True
			message = "Succesfully Fetched Queries"
		except Exception as e:
			status = False
			message = str(e)
		return {"response": res,"status":status,"message":message} 

	def get_user_details(self,id):
		conn,cursor = self.db_conn.init_conn()

		query = f"SELECT * FROM users where id = {id}"

		cursor.execute(query)

		res = cursor.fetchone()

		return res

	def create_user(self,user):
		conn,cursor = self.db_conn.init_conn()

		query = f'''INSERT INTO `users`
					(`first_name`,
					`last_name`,
					`email`,
					`password`,
					`status`)
					VALUES
					('{user.get("first_name")}',
					'{user.get("last_name")}',
					'{user.get("email")}',
					'{user.get("password")}',
					{user.get("status")})'''

		res = cursor.execute(query)

		return res

	def update_user(self,id,user):
		pass

	def delete_user(self,id):
		pass

	def check_login(self,email,password):
		conn,cursor = self.db_conn.init_conn()

		resp = {}
		res = None
		status = False
		message = ""
		try:
			query = f'SELECT * FROM users where email = "{email}" and password = "{password}";'

			print(query)
			cursor.execute(query)

			res = cursor.fetchone()
			if res:
				status = True
				message = "Succesfully logged in..."
			else:
				status = False
				message = "Invalid Login credentials"
		except Exception as e:
			status = False
			message = str(e)
		return {"response": res,"status":status,"message":message} 
