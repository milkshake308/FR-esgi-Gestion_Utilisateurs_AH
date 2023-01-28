CREATE TABLE users(
user_id INT AUTO_INCREMENT PRIMARY KEY,
login VARCHAR(255) NOT NULL UNIQUE,
user_firstname VARCHAR(255) NOT NULL,
user_lastname VARCHAR(255) NOT NULL,
hashed_password VARCHAR(255) NOT NULL,
password_timestamp TIMESTAMP NOT NULL
);

CREATE TABLE groups
(group_id INT AUTO_INCREMENT PRIMARY KEY,
group_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE user_membership(
user_membership_id INT AUTO_INCREMENT PRIMARY KEY,
group_id INT REFERENCES groups(group_id),
user_id INT REFERENCES users(user_id)
);
