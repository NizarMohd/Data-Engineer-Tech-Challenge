SELECT membership_id
FROM transaction
GROUP BY membership_id
ORDER BY SUM(price) DESC
LIMIT 10;
