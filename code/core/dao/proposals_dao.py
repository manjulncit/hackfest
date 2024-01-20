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

			res = self.get_column_value_pair(cursor)
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
			query = ''' INSERT INTO `proposals`
                        (`identifier`,
                        `title`,
                        `category`,
                        `description`,
                        `team_member_count`,
                        `status`)
                        VALUES
                        (
                        "33ac0b9f-d092-4603-bf68-9e77bcee0f33",
                        "First Proposal",
                        "Technology",
                        "This is a sample first proposal",
                        4,
                        1);
                        '''
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
	def get_column_value_pair(self,cursor):
		columns = cursor.description
		result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		return result
