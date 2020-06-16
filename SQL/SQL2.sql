-- AGGREGATE FUNCTIONS

-- Count

-- COUNT() is a function that takes the name of a column as an argument and counts the number of non-empty values in that column.

SELECT COUNT(*) 
FROM fake_apps
WHERE price = 0;

-- Sum
-- SQL makes it easy to add all values in a particular column using SUM().

SELECT SUM(downloads)
FROM fake_apps;

-- Max / Min
-- The MAX() and MIN() functions return the highest and lowest values in a column, respectively.

SELECT MAX(price)
FROM fake_apps;

SELECT MIN(downloads)
FROM fake_apps;


-- Average
-- SQL uses the AVG() function to quickly calculate the average value of a particular column.

SELECT AVG(price)
FROM fake_apps;

SELECT AVG(downloads)
FROM fake_apps;


-- ROUND


SELECT name, ROUND(price, 0)
FROM fake_apps;

SELECT ROUND(AVG(price), 2)
FROM fake_apps;


-- Group By I
-- GROUP BY is a clause in SQL that is used with aggregate functions
-- The GROUP BY statement comes after any WHERE statements, but before ORDER BY or LIMIT.

SELECT price, COUNT(*) 
FROM fake_apps
WHERE downloads >= 20000
GROUP BY price;

SELECT  category, SUM(downloads)
FROM fake_apps
GROUP BY category;

-- Group By II

-- SQL lets us use column reference(s) in our GROUP BY that will make our lives easier.

SELECT category, 
   price,
   AVG(downloads)
FROM fake_apps
GROUP BY 1, 2;

-- 1 is the first column selected
-- 2 is the second column selected
-- 3 is the third column selected and so on.


-- HAVING 

-- HAVING is very similar to WHERE.
-- In fact, all types of WHERE clauses you learned about thus far can be used with HAVING

SELECT price, 
   ROUND(AVG(downloads)),
   COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(*) > 10;


-- Code challenge

SELECT COUNT(*)
FROM users
WHERE email LIKE '%.com';


SELECT first_name, COUNT(*) AS 'count'
FROM users

GROUP BY first_name
ORDER BY  2 DESC;


SELECT
  ROUND(watch_duration_in_minutes,0) as duration,
  COUNT(*) as count
FROM watch_history
GROUP BY duration
ORDER BY duration ASC;

SELECT user_id, SUM(amount) AS amount
FROM payments
WHERE status = 'paid'
GROUP BY user_id
ORDER BY amount DESC;

SELECT
  user_id,
  sum(watch_duration_in_minutes) AS time
FROM watch_history
GROUP BY user_id
HAVING time > 400;

SELECT ROUND(SUM(watch_duration_in_minutes), 0) AS minutes
FROM watch_history;

SELECT pay_date AS day, SUM(amount) AS total
FROM payments
WHERE status = 'paid'
GROUP BY day
ORDER BY total DESC;

SELECT AVG(amount) AS average
FROM payments
WHERE status = 'paid'; 

SELECT
  MAX(watch_duration_in_minutes) AS max,
  MIN(watch_duration_in_minutes) AS min
FROM watch_history;



-- Project Trends in Startups

SELECT *
FROM startups;

SELECT COUNT(*)
FROM startups;

SELECT SUM(valuation)
FROM startups;

SELECT MAX(raised)
FROM startups;

SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded)
FROM startups;

SELECT AVG(valuation)
FROM startups;

SELECT AVG(valuation)
FROM startups
GROUP BY category;

SELECT ROUND(AVG(valuation),2)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY 1
ORDER BY 2 DESC;

SELECT category, COUNT(*)
FROM startups
GROUP BY category;

SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3;

SELECT location, AVG(employees)
FROM startups
GROUP BY location;

SELECT location, AVG(employees)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;



-- Project How to Hack Hacker News

 SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

SELECT SUM(score)
FROM hacker_news;

SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

SELECT (517 + 309 + 304 + 282) / 6366.0;

SELECT user,
   COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY 1
ORDER BY 2 DESC;

SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source'
FROM hacker_news;

SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;

SELECT timestamp
FROM hacker_news
LIMIT 10;

SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

SELECT strftime('%H', timestamp), 
   AVG(score),
   COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 1;


SELECT strftime('%H', timestamp) AS 'Hour', 
   ROUND(AVG(score), 1) AS 'Average Score', 
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 1;


-- Project The Metropolitan Museum of Art

 SELECT *
FROM met
LIMIT 10;

SELECT COUNT(*)
FROM met;

SELECT COUNT(*)
FROM met
WHERE category LIKE '%celery%';

SELECT DISTINCT category
FROM met
WHERE category LIKE '%celery%';

SELECT date, title, medium
FROM met
WHERE date LIKE '%1600%';

SELECT country, COUNT(*)
FROM met
WHERE country IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

SELECT category, COUNT(*)
FROM met
GROUP BY 1
HAVING COUNT(*) > 100;

SELECT CASE
   WHEN medium LIKE '%gold%'   THEN 'Gold'
   WHEN medium LIKE '%silver%' THEN 'Silver'
   ELSE NULL
  END AS 'Bling',
  COUNT(*)
FROM met
WHERE Bling IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;


-- Project Cryptocurrency Exchange

 SELECT *
FROM transactions;

SELECT SUM(money_in)
FROM transactions;

SELECT SUM(money_out)
FROM transactions;

SELECT COUNT(money_in)
FROM transactions
WHERE currency = 'BIT';

SELECT MAX(money_in)
FROM transactions;

SELECT MAX(money_out)
FROM transactions;

SELECT AVG(money_in)
FROM transactions
WHERE currency = 'ETH';

SELECT date, 
   AVG(money_in), 
   AVG(money_out)
FROM transactions
GROUP BY date;

