from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from core.routes.users import users
app.register_blueprint(users)

from core.routes.proposals import proposals
app.register_blueprint(proposals)

from core.routes.api.api_proposals import api_proposals
app.register_blueprint(api_proposals)

from core.routes.api.rest_api_proposals import rest_api_proposals
app.register_blueprint(rest_api_proposals)

if __name__ == '__main__':
    app.run(debug=True)