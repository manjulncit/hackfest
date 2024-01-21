> Database CRUD

- Users
	- Constraints
		- Primary Key (PK)
		- Unique Key
		- Foreign Key (FK)
		- Auto Increment (AI)
		- Not Null (NN)

	- Columns
		- id			PK			NN 
		- first_name
		- last_name
		- email
		- password
		- status

-- INSERT : CREATE
INSERT INTO `db_hackfest`.`users`
(`first_name`,
`last_name`,
`email`,
`password`,
`status`)
VALUES
('Test',
'Test',
'test@gmail.com',
'test123',
1);

-- SELECT : RETRIEVE
SELECT * FROM db_hackfest.users;

-- UPDATE
UPDATE `db_hackfest`.`users`
SET
`first_name` = 'Kushal',
`last_name` = 'Ghimire',
`email` = 'kushal@gmail.com',
`password` = 'kushal123',
`status` = '1'
WHERE `id` = '3';


-- DELETE
DELETE FROM `db_hackfest`.`users`
WHERE id = 3;


-- Login
SELECT * FROM users WHERE email = 'manjul@gmail.com' and password = 'manjul123';


Sample tables:
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

-- JOIN QUERY:
SELECT * FROM users u 
JOIN proposals p
ON u.id = p.user_id