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

		res = None
		status = False
		message = ""
		try:
			query = f"SELECT * FROM proposals where id = {proposal_id};"

			cursor.execute(query)

			res = self.get_column_value_pair(cursor)
			status = True
			message = "Succesfully Fetched Proposal Details"
		except Exception as e:
			message = str(e)
		return {"response": res[0],"status":status,"message":message} 

	def create_proposal(self,proposal):
		conn,cursor = self.db_conn.init_conn()
		res = None
		status = False
		message = ""

		try:
			#TODO: Update with the right query
			query = f''' INSERT INTO `proposals`
                        (`identifier`,
                        `title`,
                        `category`,
                        `description`,
                        `team_member_count`,
                        `status`)
                        VALUES
                        (
                        "{proposal.get('identifier')}",
                        "{proposal.get('title')}",
                        "{proposal.get('category')}",
                        "{proposal.get('description')}",
                        "{proposal.get('member_count')}",
                        1);
                        '''
			res = cursor.execute(query)
			status = True
			message = "Succesfully Created Proposal"
		except Exception as e:
			message = str(e)		

		return {"response": res,"status":status,"message":message} 

	def update_proposal(self,proposal_id,proposal):
		conn,cursor = self.db_conn.init_conn()
		res = None
		status = False
		message = ""
		print(proposal)
		try:
			query = f''' UPDATE `proposals`
                        SET
                        `title` = "{proposal.get("title")}",
                        `description` = "{proposal.get("description")}",
                        `category` = "{proposal.get("category")}",
                        `team_member_count` = "{proposal.get("member_count")}"
                        WHERE `id` = '{proposal_id}';'''
			print(query)
			res = cursor.execute(query)
			status = True
			message = "Succesfully Updated Proposal"
		except Exception as e:
			message = str(e)		

		return {"response": res,"status":status,"message":message} 

	def delete_proposal(self,proposal_id):
		conn,cursor = self.db_conn.init_conn()
		res = None
		status = False
		message = ""

		try:
			query = f'''DELETE FROM `proposals`
                        WHERE id = {proposal_id};'''
			res = cursor.execute(query)
			status = True
			message = "Succesfully Deleted Proposal"
		except Exception as e:
			message = str(e)		

		return {"response": res,"status":status,"message":message} 
	def get_column_value_pair(self,cursor):
		columns = cursor.description
		result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		return result
