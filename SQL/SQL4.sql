--What is a Funnel?
--In the world of marketing analysis, “funnel” is a word you will hear time and time again.
-- A funnel is a marketing model which illustrates the theoretical customer journey towards the purchase of a product or service. Oftentimes, we want to track how many users complete a series of steps and know which steps have the most number of users giving up.
-- Some examples include:
-- Answering each part of a 5 question survey on customer satisfaction


SELECT * 
 FROM  survey_responses
 LIMIT 10;


SELECT question_text,
   COUNT(DISTINCT user_id)
FROM survey_responses
GROUP BY 1;


SELECT *
 FROM onboarding_modals
 LIMIT 10;

 SELECT modal_text, COUNT(DISTINCT user_id)
 FROM onboarding_modals
GROUP BY 1
ORDER BY 1;

SELECT modal_text,
  COUNT(DISTINCT CASE
    WHEN ab_group = 'control' THEN user_id
    END) AS 'control_clicks',
  COUNT(DISTINCT CASE
    WHEN ab_group = 'variant' THEN user_id
    END) AS 'variant_clicks'
FROM onboarding_modals
GROUP BY 1
ORDER BY 1;

SELECT DISTINCT b.browse_date,
   b.user_id,
   c.user_id IS NOT NULL AS 'is_checkout',
   p.user_id IS NOT NULL AS 'is_purchase'
FROM browse AS 'b'
LEFT JOIN checkout 'c'
  ON c.user_id = b.user_id
LEFT JOIN purchase 'p'
  ON p.user_id = c.user_id
LIMIT 50;

WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
SELECT COUNT(*) AS 'num_browse',
   SUM(is_checkout) AS 'num_checkout',
   SUM(is_purchase) AS 'num_purchase)',
   1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
   1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase'
FROM funnels;


WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
SELECT browse_date,
   COUNT(*) AS 'num_browse',
   SUM(is_checkout) AS 'num_checkout',
   SUM(is_purchase) AS 'num_purchase',
   1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
   1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase'
FROM funnels
GROUP BY browse_date
ORDER BY browse_date;

-- Project Usage Funnels with Warby Parker

 SELECT *
 FROM survey
 LIMIT 10;

 SELECT question,
   COUNT(DISTINCT user_id)
FROM survey
GROUP BY 1;

SELECT *
FROM quiz
LIMIT 5;

SELECT *
FROM home_try_on
LIMIT 5;

SELECT *
FROM purchase
LIMIT 5;

SELECT DISTINCT q.user_id,
   h.user_id IS NOT NULL AS 'is_home_try_on',
   h.number_of_pairs,
   p.user_id IS NOT NULL AS 'is_purchase'
FROM quiz q
LEFT JOIN home_try_on h
   ON q.user_id = h.user_id
LEFT JOIN purchase p
   ON p.user_id = q.user_id
LIMIT 10;


-- CHURN

SELECT 1.0 * 
(
  SELECT COUNT(*)
  FROM subscriptions
  WHERE subscription_start < '2017-01-01'
  AND (
    subscription_end
    BETWEEN '2017-01-01'
    AND '2017-01-31'
  )
) / (
  SELECT COUNT(*) 
  FROM subscriptions 
  WHERE subscription_start < '2017-01-01'
  AND (
    (subscription_end >= '2017-01-01')
    OR (subscription_end IS NULL)
  )
) 
AS result;

WITH enrollments AS 
(SELECT *
FROM subscriptions
WHERE subscription_start < '2017-01-01'
AND (
  (subscription_end >= '2017-01-01')
  OR (subscription_end IS NULL)
)),
status AS 
(SELECT 
CASE
  WHEN (subscription_end > '2017-01-31')
    OR (subscription_end IS NULL) THEN 0
  ELSE 1
  END as is_canceled,
CASE
  WHEN (subscription_start < '2017-01-01')
    AND (
      (subscription_end >= '2017-01-01')
        OR (subscription_end IS NULL)
    ) THEN 1
    ELSE 0
  END as is_active
FROM enrollments
)
SELECT 1.0 * SUM(is_canceled)/SUM(is_active) FROM status;

WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
CASE 
  WHEN subscription_end BETWEEN first_day AND last_day THEN 1
  ELSE 0
END as is_canceled
FROM cross_join),
status_aggregate AS
(SELECT
  month,
  SUM(is_active) as active,
  SUM(is_canceled) as canceled
FROM status
GROUP BY month)
SELECT
  month,
  1.0 * canceled/active AS churn_rate
FROM status_aggregate;
SELECT *
FROM status
LIMIT 100;

--

 --SELECT *
 --FROM subscriptions
 --LIMIT 100;

 SELECT MAX(subscription_start) ,
 MIN(subscription_start)
 FROM subscriptions

WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
)

cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    )

CASE
  WHEN (subscription_start < first_day) 
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active

CASE 
  WHEN subscription_end BETWEEN first_day AND last_day THEN 1
  ELSE 0
END as is_canceled

status_aggregate AS
(SELECT
  month,
  SUM(is_active) as active,
  SUM(is_canceled) as canceled
FROM status
GROUP BY month)

SELECT
  month,
  1.0 * canceled/active AS churn_rate
FROM status_aggregate;
SELECT *
FROM status
LIMIT 100;

-- FIRST- AND LAST-TOUCH ATTRIBUTION using UTM 
-- UTM parameters are a way of tracking visits to a website

SELECT *
FROM page_visits
WHERE user_id = 10069;

-- The Attribution Query I
-- In order to get first-touch attributions
SELECT user_id,
   MIN(timestamp) AS 'first_touch_at'
FROM page_visits
GROUP BY user_id;

SELECT user_id,
  MAX(timestamp) AS 'last_touch_at'
FROM page_visits
WHERE user_id = 10069
GROUP BY user_id;

-- The Attribution Query II

WITH first_touch AS (
   SELECT user_id,
      MIN(timestamp) AS 'first_touch_at'
   FROM page_visits
   GROUP BY user_id)
SELECT ft.user_id,
  ft.first_touch_at,
  pv.utm_source
FROM first_touch AS 'ft'
JOIN page_visits AS 'pv'
  ON ft.user_id = pv.user_id
  AND ft.first_touch_at = pv.timestamp;


-- ANALYZE REAL DATA WITH SQL
-- 
/*
Here's the first-touch query, in case you need it
*/

WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT ft.user_id,
    ft.first_touch_at,
    pv.utm_source,
		pv.utm_campaign
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp;
