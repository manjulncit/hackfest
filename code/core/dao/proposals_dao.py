from core.db.db_connection import DBConnection

class ProposalDAO():

	def __init__(self):
		self.db_conn = DBConnection()

	def list_proposals(self):
		conn,cursor = self.db_conn.init_conn()

		res = None
		status = False
		message = ""
		try:
			query = "SELECT * FROM proposals;"

			cursor.execute(query)

			res = cursor.fetchall()
			status = True
			message = "Succesfully Fetched Queries"
		except Exception as e:
			message = str(e)
		return {"response": res,"status":status,"message":message} 

	def get_proposal_details(self,proposal_id):
		conn,cursor = self.db_conn.init_conn()

		query = f"SELECT * FROM proposals where id = {proposal_id}"

		cursor.execute(query)

		res = cursor.fetchone()

		return res

	def create_proposal(self,proposal):
		conn,cursor = self.db_conn.init_conn()
		res = None
		status = False
		message = ""

		try:
			#TODO: Update with the right query
			query = f''''''
			res = cursor.execute(query)
			status = True
			message = "Succesfully Created Proposal"
		except Exception as e:
			message = str(e)		

		return {"response": res,"status":status,"message":message} 

	def update_proposal(self,proposal_id,proposal):
		pass

	def delete_proposal(self,proposal_id):
		pass
