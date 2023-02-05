CREATE TABLE pf_users(
    user_id             INT             AUTO_INCREMENT  PRIMARY KEY,
    login               VARCHAR(255)    NOT NULL        UNIQUE,
    user_firstname      VARCHAR(255)    NULL,
    user_lastname       VARCHAR(255)    NULL,
    hashed_password     VARCHAR(255)    NOT NULL,
    password_timestamp  TIMESTAMP       NOT NULL        DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE pf_groups(
    group_id    INT             AUTO_INCREMENT  PRIMARY KEY,
    group_name  VARCHAR(255)    NOT NULL        UNIQUE
);

CREATE TABLE pf_user_membership(
    user_membership_id  INT     AUTO_INCREMENT  PRIMARY KEY,
    group_id            INT     REFERENCES  pf_groups(group_id),
    user_id             INT     REFERENCES  pf_users(user_id)
);
INSERT INTO pf_users(login, hashed_password) VALUES ('admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918');
INSERT INTO pf_groups(group_name) VALUES ('admins');
INSERT INTO pf_groups(group_name) VALUES ('users');
INSERT INTO pf_user_membership(group_id, user_id) VALUES (1, 1);