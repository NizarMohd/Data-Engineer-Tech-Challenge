SELECT item_bought, COUNT(*) as total_bought
FROM transaction
GROUP BY item_bought
ORDER BY total_bought DESC
LIMIT 3;