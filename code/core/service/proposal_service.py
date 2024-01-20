from core.dao.proposals_dao import ProposalDAO

class ProposalService():

	def __init__(self):
		self.dao = ProposalDAO()

	def list_proposals(self):
		return self.dao.list_proposals()

	def get_proposal_details(self,proposal_id):
		return self.dao.get_proposal_details(proposal_id)

	def create_proposal(self,proposal):
		return self.dao.create_proposal(proposal)
	
	def update_proposal(self,proposal_id,proposal):
		return self.dao.update_proposal(proposal_id,proposal)

	def delete_proposal(self,proposal_id):
		return self.dao.delete_proposal(proposal_id)