from flask import Blueprint,request,render_template,redirect,jsonify

rest_api_proposals = Blueprint('rest_api_proposals', __name__)

from core.service.proposal_service import ProposalService

@rest_api_proposals.route('/api/v2/proposals',methods=['POST'])
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
 
@rest_api_proposals.route('/api/v2/proposals',methods=['GET'])
def list_proposal():
    proposal_service = ProposalService()
    res = proposal_service.list_proposals()
    if res.get('status'):
        proposals = res.get("response")
        response = {"res":proposals,"status": True}
    else:
        response = {"res":None,"status": False,"message":res.get("message")}
    return jsonify(response)

@rest_api_proposals.route('/api/v2/proposals/<proposal_id>',methods=['PUT'])
def update(proposal_id):
    proposal_service = ProposalService()
    req = request.json
    title = req.get("title")
    category = req.get("category")
    description = req.get("description")
    member_count = req.get("member_count")
    proposal = {"title": title,"category":category,"description":description,"member_count":member_count}
    res = proposal_service.update_proposal(proposal_id,proposal)
    return jsonify(res)

@rest_api_proposals.route('/api/v2/proposals/<proposal_id>',methods=['DELETE'])
def delete(proposal_id):
    proposal_service = ProposalService()
    res = proposal_service.delete_proposal(proposal_id)
    return jsonify(res)

@rest_api_proposals.route('/api/v2/proposals/<proposal_id>',methods=['GET'])
def view_details(proposal_id):
    proposal_service = ProposalService()
    res = proposal_service.get_proposal_details(proposal_id)
    return jsonify(res)