-- The most commonly used SQL commands to query a table in a database.

-- Fun fact: IBM started out SQL as SEQUEL (Structured English QUEry Language) in the 1970’s to query databases.

-- Select
-- We can select individual columns by their names (separated by a comma):

SELECT name, genre ,year 
FROM movies;


-- AS
-- AS is a keyword in SQL that allows you to rename a column or table using an alias.
SELECT imdb_rating AS 'IMDb'
FROM movies;

SELECT name AS 'Movies Titles'
FROM movies;
-- Although it’s not always necessary, it’s best practice to surround your aliases with single quotes.
-- When using AS, the columns are not being renamed in the table. The aliases only appear in the result.


-- DISTINCT is used to return unique values in the output. It filters out all duplicate values in the specified column(s).
SELECT DISTINCT year
FROM movies;


# Where
#We can restrict our query results using the WHERE clause in order to obtain only the information we want.


SELECT * 
FROM movies 
WHERE imdb_rating > 5;

SELECT * 
FROM movies 
WHERE year > 2014;


-- Like I

 -- LIKE can be a useful operator when you want to compare similar values.

SELECT * 
FROM movies
WHERE name LIKE 'Se_en';

-- This will select the titles Seven and Se7en from the movies table

--Like II
-- The percentage sign % is another wildcard character that can be used with LIKE.

-- This statement below filters the result set to only include movies with names that begin with the letter ‘A’:

SELECT * 
FROM movies
WHERE name LIKE 'A%';


-- A% matches all movies with names that begin with letter ‘A’
-- %a matches all movies that end with ‘a’
-- We can also use % both before and after a pattern:

SELECT * 
FROM movies 
WHERE name LIKE '%man%';

-- Here, any movie that contains the word ‘man’ in its name will be returned in the result.

-- LIKE is not case sensitive.

SELECT * 
FROM movies
WHERE name LIKE 'The %';


-- Is Null

-- IS NULL
-- IS NOT NULL

SELECT name
FROM movies 
WHERE imdb_rating IS NOT NULL;

--Between
-- The BETWEEN operator is used in a WHERE clause to filter the result set within a certain range. 
 -- It accepts two values that are either numbers, text or dates.

SELECT *
FROM movies
WHERE name BETWEEN 'D' AND 'G';

SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979;


-- And
-- Sometimes we want to combine multiple conditions. we use the AND operator to combine multiple conditions.

SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979
  AND imdb_rating > 8;


SELECT *
FROM movies
WHERE year < 1985
   AND genre = 'horror';


-- Or

SELECT *
FROM movies
WHERE  genre = 'comedy'
   OR genre = 'romance';


SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';



-- Order By

-- We can sort the results using ORDER BY, either alphabetically or numerically.

SELECT *
FROM movies
WHERE imdb_rating > 8
ORDER BY year DESC;

SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;



-- limit
-- LIMIT is a clause that lets you specify the maximum number of rows the result set will have.

SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;


-- Case
-- A CASE statement allows us to create different outputs (usually in the SELECT statement). It is SQL’s way of handling if-then logic.

SELECT name,
 CASE
  WHEN genre = 'romance' THEN 'Chill'
  WHEN genre = 'comedy'  THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;

SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END AS 'Review'
FROM movies;


-- CODE CHALLENGE: QUERIES



SELECT name 
FROM babies
WHERE name LIKE 'S%'
LIMIT  20;

SELECT name,gender,number
FROM babies
WHERE year = 1880 
ORDER BY number DESC
LIMIT 10;


SELECT *
FROM nomnom
WHERE cuisine = 'Japanese'
  AND price = '$$';


 SELECT * 
 FROM nomnom
WHERE name LIKE '%noodle%';

 SELECT *
FROM nomnom
WHERE health IS NULL;


SELECT title, publisher
 FROM news
 ORDER BY title;


  SELECT *
 FROM news
 WHERE title LIKE '%bitcoin%';

 SELECT *
FROM news
WHERE category = 'b'
ORDER BY timestamp DESC
LIMIT 20;




-- Project New York Restaurants

SELECT *
FROM nomnom;

SELECT DISTINCT neighborhood
FROM nomnom;

SELECT DISTINCT cuisine
FROM nomnom;

SELECT *
FROM nomnom
WHERE cuisine = 'Chinese';

SELECT *
FROM nomnom
WHERE review >= 4;

SELECT *
FROM nomnom
WHERE cuisine = 'Italian'
   AND price LIKE '%$$$%';


SELECT *
FROM nomnom
WHERE name LIKE '%meatball%';

ELECT *
FROM nomnom
WHERE neighborhood = 'Midtown'
   OR neighborhood = 'Downtown'
   OR neighborhood = 'Chinatown'; 

SELECT *
FROM nomnom
WHERE health IS NULL;


SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 10;

SELECT name,
 CASE
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
 END AS 'Review'
FROM nomnom;


-- Project RPA Fraud Detection

 SELECT *
FROM transaction_data
LIMIT 10;

SELECT full_name, email, zip
FROM transaction_data
WHERE zip = 20252;

SELECT full_name, email
FROM transaction_data
WHERE full_name = 'Art Vandelay'
   OR full_name LIKE '% der %';

SELECT ip_address, email
FROM transaction_data
WHERE ip_address LIKE '10.%';

SELECT email
FROM transaction_data
WHERE email LIKE '%temp_email.com';

SELECT *
FROM transaction_data
WHERE full_name LIKE 'John%'
  AND ip_address LIKE '120.%';


-- Project RPA Customer Segmentation

 SELECT *
FROM users
LIMIT 20;

SELECT email, birthday
FROM users
WHERE birthday BETWEEN '1980-01-01' AND '1989-12-31';

SELECT email, created_at
FROM users
WHERE created_at <= '2017-04-30';

ELECT email
FROM users
WHERE test = 'bears';

SELECT email
FROM users
WHERE campaign LIKE 'BBB%';

SELECT email
FROM users
WHERE campaign LIKE '%-2';

SELECT email
FROM users
WHERE campaign IS NOT NULL
  AND test IS NOT NULL;




-- Project Davie's Burgers Subway Ad

 SELECT *
FROM orders
LIMIT 10;

ELECT DISTINCT order_date
FROM orders
ORDER BY order_date DESC;

SELECT special_instructions
FROM orders
LIMIT 20;

SELECT special_instructions
FROM orders
WHERE special_instructions IS NOT NULL;

SELECT special_instructions
FROM orders
WHERE special_instructions IS NOT NULL
ORDER BY special_instructions;

SELECT special_instructions
FROM orders
WHERE special_instructions LIKE '%sauce%';

SELECT special_instructions
FROM orders
WHERE special_instructions LIKE '%door%';

SELECT special_instructions
FROM orders
WHERE special_instructions LIKE '%box%';

SELECT id AS '#',
   special_instructions AS 'Notes'
FROM orders
WHERE special_instructions LIKE '%box%';


