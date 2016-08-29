DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(200),
    password VARCHAR(200),
    email VARCHAR(200),
    user_level INT NOT NULL
);

INSERT INTO users(
    username,
    password,
    email,
    user_level)
VALUES(
    'admin',
    'admin',
    'admin@admin.com',
    '1');

INSERT INTO users(
    username,
    password,
    email,
    user_level)
VALUES(
    'developer',
    'developer',
    'oniioniichan@gmail.com',
    '2');