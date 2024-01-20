from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from core.routes.users import users
app.register_blueprint(users)

from core.routes.proposals import proposals
app.register_blueprint(proposals)

if __name__ == '__main__':
    app.run(debug=True)