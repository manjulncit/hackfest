from flask import Blueprint,request,render_template,redirect

from core.service.user_service import UserService

#TODO: Remove this
import mysql.connector

users = Blueprint('users', __name__)

@users.route('/')
def hello_world():
    return render_template('pages/home.html')
 
@users.route('/login')
def login():
    return render_template('pages/login.html')

@users.route('/register')
def register():
    return render_template('pages/register.html')

@users.route('/forgot-password')
def forgot_password():
    return render_template('pages/forgot-password.html')

@users.route('/doLogin',methods=['POST'])
def do_login():
    user_service = UserService()

    email = request.form['email']
    password = request.form['password']

    res = user_service.check_login(email,password)
    
    if res.get("status"):
        return redirect('/')
    else:
        return redirect('/login')

@users.route('/doRegister',methods=['POST'])
def do_register():
    user_service = UserService()

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    data = {"first_name": first_name,"last_name":last_name,"email":email,"password":password}
    res = user_service.register_user(data)
    print(res)
    if res.get("status"):
        return redirect('/login')
    else:
        return redirect('/register')