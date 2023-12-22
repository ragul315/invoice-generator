-- Connect to MySQL and create a new database named 'billing'
CREATE DATABASE billing;

-- Switch to the 'billing' database
USE billing;

-- Create the 'users' table to store user credentials
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- (Optional) Create a sample invoice table for testing purposes
CREATE TABLE invoice_sample (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL
);

-- (Optional) Insert a sample user into the 'users' table for testing the login functionality
INSERT INTO users (username, password) VALUES ('sample_user', 'sample_password');

-- Grant all privileges to the MySQL user for the 'billing' database
GRANT ALL PRIVILEGES ON billing.* TO 'root'@'localhost';
