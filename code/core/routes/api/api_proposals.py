from flask import Blueprint,request,render_template,redirect,jsonify

api_proposals = Blueprint('api_proposals', __name__)

from core.service.proposal_service import ProposalService

@api_proposals.route('/api/v1/create_proposals',methods=['POST'])
def create():
    if request.method == 'POST':
        req = request.json
        title = req.get("title")
        category = req.get("category")
        description = req.get("description")
        member_count = req.get("member_count")

        proposal = {"title": title,"category":category,"description":description,"member_count":member_count}
        proposal_service = ProposalService()
        res = proposal_service.create_proposal(proposal)
        return jsonify(res)
 
@api_proposals.route('/api/v1/proposals')
def list_proposal():
    proposal_service = ProposalService()
    res = proposal_service.list_proposals()
    if res.get('status'):
        proposals = res.get("response")
        response = {"res":proposals,"status": True}
    else:
        response = {"res":None,"status": False,"message":res.get("message")}
    return jsonify(response)

@api_proposals.route('/api/v1/proposals_update/<proposal_id>',methods=['POST'])
def update(proposal_id):
    proposal_service = ProposalService()
    if request.method == 'POST':
        req = request.json
        title = req.get("title")
        category = req.get("category")
        description = req.get("description")
        member_count = req.get("member_count")

        proposal = {"title": title,"category":category,"description":description,"member_count":member_count}
        res = proposal_service.update_proposal(proposal_id,proposal)
        return jsonify(res)

@api_proposals.route('/api/v1/proposals_delete/<proposal_id>')
def delete(proposal_id):
    proposal_service = ProposalService()
    res = proposal_service.delete_proposal(proposal_id)
    return jsonify(res)

@api_proposals.route('/api/v1/proposal_details/<proposal_id>')
def view_details(proposal_id):
    proposal_service = ProposalService()
    res = proposal_service.get_proposal_details(proposal_id)
    return jsonify(res)