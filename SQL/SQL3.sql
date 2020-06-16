-- MULTIPLE TABLES

SELECT *
FROM orders
LIMIT 5;

SELECT *
FROM subscriptions
LIMIT 5;

SELECT * 
FROM customers
LIMIT 5;


-- Combining Tables With SQL


SELECT *
FROM orders
JOIN subscriptions
  ON orders.subscription_id = subscriptions.subscription_id;

  SELECT *
FROM orders
JOIN subscriptions
  ON orders.subscription_id = subscriptions.subscription_id
WHERE subscriptions.description = 'Fashion Magazine';

-- Inner Joins

SELECT COUNT(*)
FROM newspaper;

SELECT COUNT(*)
FROM online;


SELECT COUNT(*)
FROM newspaper
JOIN online
  ON newspaper.id = online.id;


-- Left Joins

SELECT * 
FROM newspaper 
LEFT JOIN online
  ON newspaper.id = online.id;



SELECT * 
FROM newspaper 
LEFT JOIN online
  ON newspaper.id = online.id
WHERE online.id IS NULL;


-- Primary Key vs Foreign Key

SELECT *
FROM classes
JOIN students
  ON classes.id = students.class_id;


-- Cross Join

SELECT COUNT(*)
FROM newspaper
WHERE start_month <= 3
  AND  end_month >= 3;

SELECT *
FROM newspaper
CROSS JOIN months;


SELECT *
FROM newspaper
CROSS JOIN months
WHERE start_month <= month AND end_month >= month;

SELECT month, COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE start_month <= month AND end_month >= month
GROUP BY month;


-- Union
-- Sometimes we just want to stack one dataset on top of the other. Well, the UNION operator allows us to do that.
-- Tables must have the same number of columns.
-- The columns must have the same data types in the same order as the first table.

SELECT *
FROM newspaper
UNION
SELECT * 
FROM online;

-- With

WITH previous_query AS (
   SELECT customer_id,
      COUNT(subscription_id) AS 'subscriptions'
   FROM orders
   GROUP BY customer_id
)
SELECT customers.customer_name, 
   previous_query.subscriptions
FROM previous_query
JOIN customers
  ON previous_query.customer_id = customers.customer_id;



-- SONGIFY CODE CHALLENGE

SELECT premium_users.user_id,
   plans.description
FROM premium_users
JOIN plans
  ON plans.id = premium_users.membership_plan_id;


SELECT plays.user_id,
   plays.play_date,
   songs.title
FROM plays
JOIN songs
  ON plays.song_id = songs.id;


 SELECT users.id
FROM users
LEFT JOIN premium_users
  ON users.id =premium_users.user_id
WHERE premium_users.user_id IS NULL;

WITH january AS (
  SELECT *
  FROM plays
  WHERE strftime("%m", play_date) = '01'
),
february AS (
  SELECT *
  FROM plays
  WHERE strftime("%m", play_date) = '02'

)
SELECT january.user_id
FROM january
LEFT JOIN february
	ON january.user_id = february.user_id
WHERE february.user_id IS NULL;

SELECT premium_users.user_id,
	premium_users.purchase_date,
  premium_users.cancel_date,
  months.months
FROM premium_users
CROSS JOIN months;

SELECT premium_users.user_id,
  months.months,
  CASE
    WHEN (
      premium_users.purchase_date <= months.months
      )
      AND
      (
        premium_users.cancel_date >= months.months
        OR
        premium_users.cancel_date IS NULL
      )
    THEN 'active'
    ELSE 'not_active'
  END AS 'status'

SELECT *
FROM songs
UNION 
SELECT *
FROM bonus_songs
LIMIT 10;

SELECT '2017-01-01' as month
UNION
SELECT '2017-02-01' as month
UNION
SELECT '2017-03-01' as month;


WITH play_count AS (
  SELECT song_id,
     COUNT(*) as times_played
  FROM plays
  GROUP BY song_id)
SELECT songs.title,
	songs.artist,
  play_count.times_played
FROM play_count
JOIN songs
	ON play_count.song_id = songs.id;



-- Project Multiple Tables with REBU

SELECT * FROM trips;

SELECT * FROM riders;

SELECT * FROM cars;

SELECT riders.first,
   riders.last,
   cars.model
FROM riders, cars;

SELECT trips.date, 
   trips.pickup, 
   trips.dropoff, 
   trips.type, 
   trips.cost,
   riders.first, 
   riders.last,
   riders.username
FROM trips
LEFT JOIN riders 
  ON trips.rider_id = riders.id;

SELECT *
FROM trips
JOIN cars
  ON trips.car_id = cars.id;

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

SELECT ROUND(AVG(cost), 2)
FROM trip;

SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

SELECT COUNT(*)
FROM cars
WHERE status = 'active';

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;

