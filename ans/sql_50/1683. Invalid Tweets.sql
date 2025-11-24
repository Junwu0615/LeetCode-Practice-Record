/* Write your PL/SQL query statement below */
SELECT
tweet_id
FROM Tweets
WHERE 1=1
AND LENGTH(content) > 15