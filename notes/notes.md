> Sample Problems

Few sample problems from projecteuler.net

> Virtual Environments in Python

The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

Reference: https://docs.python.org/3/library/venv.html

> Basic Commands in python virtual environment

- mkvirtualenv
- rmvirtualenv
- workon
- deactivate

> Modern Web Architecture

Reference: https://mobidev.biz/blog/web-application-architecture-types
Also refer to image attached

> HTTP Status Codes and its advantages along with categorization

Reference: https://moz.com/learn/seo/http-status-codes

> Database

Refer to DB notes

> Handling POST request via forms and via json payload in flask

- Via Forms
	title = request.form['title']
    category = request.form['category']
    description = request.form['description']
    member_count = request.form['member_count']

- Via JSON Payload
	req = request.json
	title = req.get("title")
	category = req.get("category")
	description = req.get("description")
	member_count = req.get("member_count")

> HTTP Methods

Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
GET, POST, PUT, DELETE

> REST API

Reference: https://restfulapi.net/

Example:
Resource: Proposals

GET 	/api/v2/proposals
GET 	/api/v2/proposals/<id>
POST 	/api/v2/proposals
PUT 	/api/v2/proposals
DELETE 	/api/v2/proposals


> API Documentation

Reference for API Doc: https://www.altexsoft.com/blog/api-documentation/

> HTTP vs HTTPS

Reference: https://aws.amazon.com/compare/the-difference-between-https-and-http/

> Render Template in Flask

Reference: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

> GET vs POST

https://www.w3schools.com/tags/ref_httpmethods.asp

> POST vs PUT

https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/PUT-vs-POST-Whats-the-difference





