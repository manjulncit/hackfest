from flask import Blueprint,request,render_template,redirect

users = Blueprint('users', __name__)

@users.route('/proposals/create')
def create():
    return render_template('proposals/create.html')
 
@users.route('/proposals')
def list_proposal():
    return render_template('proposals/list.html')

@users.route('/proposals/update/<proposal_id>')
def update(proposal_id):
    return render_template('proposals/update.html')

@users.route('/proposals/delete/<proposal_id>')
def delete(proposal_id):
    return render_template('pages/forgot-password.html')

@users.route('/proposals/<proposal_id>')
def view_details(proposal_id):
    return render_template('proposals/update.html')