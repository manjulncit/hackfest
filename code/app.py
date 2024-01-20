from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from core.routes.users import users
app.register_blueprint(users)

if __name__ == '__main__':
    app.run(debug=True)