CREATE TABLE users(
user_id SERIAL PRIMARY KEY,
username VARCHAR(255) NOT NULL UNIQUE,
user_firstname VARCHAR(255) NOT NULL,
user_lastname VARCHAR(255) NOT NULL,
user_email VARCHAR(255) NOT NULL UNIQUE,
hashed_password VARCHAR(255) NOT NULL UNIQUE,
password_timestamp TIMESTAMP NOT NULL
);

CREATE TABLE groups
(group_id SERIAL PRIMARY KEY,
group_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE user_membership(
user_membership_id  SERIAL PRIMARY KEY,
group_id INTEGER REFERENCES groups(group_id),
user_id INTEGER REFERENCES users(user_id)
);
