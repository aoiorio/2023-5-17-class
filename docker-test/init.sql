CREATE DATABASE dockerdb;

USE dockerdb;

CREATE TABLE user (
  id INT AUTO_INCREMENT,
  name VARCHAR(10),
  PRIMARY KEY (id)
);

INSERT INTO user (name) VALUE ('testuser');
INSERT INTO user (name) VALUE ('foo');
INSERT INTO user (name) VALUE ('bar');
INSERT INTO user (name) VALUE ('hello');
INSERT INTO user (name) VALUE ('docker');

