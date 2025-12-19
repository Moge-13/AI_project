CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(20)
);

INSERT INTO users (id, name, role) VALUES
(1, 'Alice', 'admin'),
(2, 'Bob', 'viewer');

SELECT name, role FROM users WHERE role = 'admin';
