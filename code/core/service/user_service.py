from core.dao.users_dao import UserDAO

class UserService():

	def __init__(self):
		self.dao = UserDAO()


	def get_all_users(self):
		return self.dao.get_all_users()


	def get_user_details(self,user_id):
		return self.dao.get_user_details(user_id)

	def check_login(self,email,password):
		return self.dao.check_login(email, password)

