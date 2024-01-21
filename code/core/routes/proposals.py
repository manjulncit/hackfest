from flask import Blueprint,request,render_template,redirect

proposals = Blueprint('proposals', __name__)

from core.service.proposal_service import ProposalService

@proposals.route('/create_proposals',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        member_count = request.form['member_count']

        proposal = {"title": title,"category":category,"description":description,"member_count":member_count}
        proposal_service = ProposalService()
        res = proposal_service.create_proposal(proposal)
        if res.get("status"):
            return redirect('/proposals')
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

@proposals.route('/proposals_update/<proposal_id>',methods=['GET','POST'])
def update(proposal_id):
    proposal_service = ProposalService()
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        member_count = request.form['member_count']

        proposal = {"title": title,"category":category,"description":description,"member_count":member_count}
        res = proposal_service.update_proposal(proposal_id,proposal)
        print(res)
        if res.get("status"):
            return redirect('/proposals')
        
    res = proposal_service.get_proposal_details(proposal_id)
    proposal = res.get("response")
    return render_template('proposals/update.html',proposal=proposal)
@proposals.route('/proposals_delete/<proposal_id>')
def delete(proposal_id):
    proposal_service = ProposalService()
    proposal_service.delete_proposal(proposal_id)
    return redirect("/proposals")

@proposals.route('/proposals/<proposal_id>')
def view_details(proposal_id):
    return render_template('proposals/update.html')