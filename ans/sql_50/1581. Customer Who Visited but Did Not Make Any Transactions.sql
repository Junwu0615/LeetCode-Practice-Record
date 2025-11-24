/* Write your PL/SQL query statement below */
SELECT
    T1.customer_id,
    COUNT(T1.customer_id) AS count_no_trans
FROM Visits T1
LEFT JOIN Transactions T2
    ON T1.visit_id = T2.visit_id
WHERE 1=1
AND T2.transaction_id IS NULL
GROUP BY T1.customer_id
;