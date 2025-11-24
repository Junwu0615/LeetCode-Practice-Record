/* Write your PL/SQL query statement below */
SELECT DISTINCT
AUTHOR_ID AS id
FROM Views
WHERE 1=1
AND author_id = viewer_id
ORDER BY AUTHOR_ID