-- use python_db
use python_db;

-- Create the users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insert sample rows into the users table
INSERT INTO users (username, password) VALUES ('sai', 'sai@123');
INSERT INTO users (username, password) VALUES ('radha', 'radha@123');
INSERT INTO users (username, password) VALUES ('koti','koti@123');

