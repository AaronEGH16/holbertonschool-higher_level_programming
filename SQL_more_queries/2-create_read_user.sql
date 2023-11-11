-- create new database and user with select privileges in them

CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT PRIVILEGES ON 'hbtn_0d_2' TO 'user_0d_2'@'localhost';