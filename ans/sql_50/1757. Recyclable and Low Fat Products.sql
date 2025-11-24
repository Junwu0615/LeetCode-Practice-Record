/* Write your PL/SQL query statement below */
SELECT
p.product_id
FROM Products p
WHERE 1=1
AND p.low_fats = 'Y'
AND p.recyclable = 'Y'