-- SQL is a programming language designed to manipulate and manage data stored in relational databases.

-- A relational database is a database that organizes information into one or more tables.
-- A table is a collection of data organized into rows and columns.


-- Statements

-- A statement is text that the database recognizes as a valid command. Statements always end in a semicolon ;.
 CREATE TABLE table_name (
   column_1 data_type, 
   column_2 data_type, 
   column_3 data_type
);

-- CREATE TABLE is a clause. Clauses perform specific tasks in SQL. By convention, clauses are written in capital letters.
--  Clauses can also be referred to as commands.

SELECT * FROM celebs;

-- From above SELECT and FROM are Clauses.

-- Create

-- CREATE statements allow us to create a new table in the database. 
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
);


-- Insert
--The INSERT statement inserts a new row into a table. You can use the INSERT statement when you want to add new records
INSERT INTO celebs (id, name, age) 
VALUES (1, 'Justin Bieber', 22); 

INSERT INTO celebs (id, name, age) 
VALUES (2, 'Beyonce Knowles', 33); 

INSERT INTO celebs (id, name, age) 
VALUES (3, 'Jeremy Lin', 26); 

INSERT INTO celebs (id, name, age) 
VALUES (4, 'Taylor Swift', 26); 



-- Select
--SELECT statements are used to fetch data from a database.

-- In the statement below, SELECT returns all data in the name column of the celebs table.

SELECT name FROM celebs;

-- You can also query data from all columns in a table with SELECT *.

SELECT * FROM celebs;

-- SELECT statements always return a new table called the result set.


-- Alter
--The ALTER TABLE statement adds a new column to a table.

ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT; 

SELECT * FROM celebs; 

-- Update
-- The UPDATE statement edits a row in a table.

UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4; 

UPDATE celebs 
SET twitter_handle = '@justinbieber' 
WHERE id = 1; 

UPDATE celebs 
SET twitter_handle = '@beyonce' 
WHERE id = 2;

SELECT * FROM celebs; -- To display the table


-- Delete
-- The DELETE FROM statement deletes one or more rows from a table.

DELETE FROM celebs 
WHERE twitter_handle IS NULL;

SELECT * FROM celebs; 

-- Constraints
-- Constraints that add information about how a column can be used are invoked after specifying the data type for a column.

-- The statement below sets constraints on the celebs table.

CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);

-- The statement below sets constraints on the celebs table.
-- UNIQUE columns have a different value for every row.

--NOT NULL columns must have a value

-- DEFAULT columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.

CREATE TABLE awards (
   id INTEGER PRIMARY KEY,
   recipient TEXT NOT NULL,
   award_name TEXT DEFAULT 'Grammy'
);


-- REVIEW 

--CREATE TABLE creates a new table.
--INSERT INTO adds a new row to a table.
--SELECT queries data from a table.
--ALTER TABLE changes an existing table.
--UPDATE edits a row in a table.
--DELETE FROM deletes rows from a table.


-- Project Create a table

CREATE TABLE friends (
id INTEGER,
name TEXT,
birthday DATE
);

INSERT INTO friends ( id, name , birthday)
VALUES (1, 'Jane Doe', '1990-05-30');

-- For the `DATE` data type, the format is YYYY-MM-DD.
INSERT INTO friends ( id, name , birthday)
VALUES (2, 'Lotanna Vitalis', '1998-07-10');

INSERT INTO friends ( id, name , birthday)
VALUES (3, 'Mildred Oyem', '2002-08-14');

UPDATE friends
SET name = 'Jane Smith'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'jane@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'lotanna@gmail.com'
WHERE id = 2;

UPDATE friends
SET email = 'mildred@meo.com'
WHERE id = 3;

SELECT * 
FROM friends;






