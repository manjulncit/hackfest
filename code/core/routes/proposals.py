from flask import Blueprint,request,render_template,redirect

proposals = Blueprint('proposals', __name__)

from core.service.proposal_service import ProposalService

@proposals.route('/proposals/create')
def create():
    return render_template('proposals/create.html')
 
@proposals.route('/proposals')
def list_proposal():
    proposal_service = ProposalService()
    res = proposal_service.list_proposals()
    if res.get('status'):
        proposals = res.get("response")
        print(proposals)
        return render_template('proposals/list.html',proposals=proposals)
    else:
        return redirect("/")

@proposals.route('/proposals/update/<proposal_id>')
def update(proposal_id):
    return render_template('proposals/update.html')

@proposals.route('/proposals/delete/<proposal_id>')
def delete(proposal_id):
    return render_template('pages/forgot-password.html')

@proposals.route('/proposals/<proposal_id>')
def view_details(proposal_id):
    return render_template('proposals/update.html')