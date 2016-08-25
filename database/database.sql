DROP TABLE users;
CREATE TABLE users(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, username VARCHAR(30), password VARCHAR(30), email VARCHAR(100), image BLOB, user_level INT NOT NULL);
INSERT INTO users(username, password, email, user_level) VALUES('admin', 'admin', 'admin@minad.min', '1');
INSERT INTO users(username, password, email, user_level) VALUES('developer', 'developer', 'oniioniichan@gmail.com', '2');