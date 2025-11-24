/* Write your PL/SQL query statement below */
SELECT
c.name
FROM Customer c
WHERE 1=1
AND c.referee_id != 2 or c.referee_id is NULL