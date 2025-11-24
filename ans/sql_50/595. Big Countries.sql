/* Write your PL/SQL query statement below */
SELECT
w.name,
w.population,
w.area
FROM World w
WHERE 1=1
AND (w.area >= 3000000
OR w.population >= 25000000)