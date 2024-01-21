REST API

- HTTP Methods
- HTTP Status Codes


POST /api/v1/create_proposals
POST /api/v1/update_proposals
GET /api/v1/delete_proposals
GET /api/v1/view_proposals_details
GET /api/v1/proposals


Resource: Proposals

GET 	/api/v2/proposals
GET 	/api/v2/proposals/<id>
POST 	/api/v2/proposals
Para
PUT 	/api/v2/proposals
DELETE 	/api/v2/proposals


Reference for API Doc:
https://openweathermap.org/api/one-call-3



Users
	id => PK
	first_name
	last_name
	email

Proposals
	id => PK
	identifier
	description
	title
	user_id => FK



SELECT * FROM users u 
JOIN proposals p
ON u.id = p.user_id







