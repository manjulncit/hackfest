from flask import Flask, render_template, request, redirect
 
from core.service.user_service import UserService

import mysql.connector

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('pages/home.html')
 
@app.route('/login')
def login():
    return render_template('pages/login.html')

@app.route('/register')
def register():
    return render_template('pages/register.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('pages/forgot-password.html')

@app.route('/doLogin',methods=['POST'])
def do_login():
    user_service = UserService()

    email = request.form['email']
    password = request.form['password']

    res = user_service.check_login(email,password)
    
    if res.get("status"):
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/doRegister',methods=['POST'])
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

@app.route('/testdb')
def test_db():
    user_service = UserService()
    res = user_service.get_all_users()
    return res

if __name__ == '__main__':
    app.run(debug=True)