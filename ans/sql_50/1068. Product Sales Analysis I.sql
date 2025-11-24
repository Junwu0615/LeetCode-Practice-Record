/* Write your PL/SQL query statement below */
SELECT
T2.product_name,
T1.year,
T1.price
FROM Sales T1
INNER JOIN Product T2
    ON T1.product_id = T2.product_id