SELECT u.userName
FROM Users u JOIN Posts p
ON u.uni = p.uni
WHERE LOWER(p.title) LIKE '%research%';

SELECT u.userName, t.company, t.rate
FROM Users u JOIN Posts p
    ON u.uni = p.uni
JOIN Tags t
    ON p.id = t.postId
WHERE t.company IN (
    SELECT company
    FROM Tags
    GROUP BY company
    ORDER BY AVG(rate) DESC
    LIMIT 3
);

SELECT u.userName
FROM Users u JOIN (
    SELECT uni
    FROM Comments
    GROUP BY uni
    ORDER BY COUNT(*) DESC
    LIMIT 3
    UNION
    SELECT uni
    FROM Posts
    GROUP BY uni
    ORDER BY COUNT(*) DESC
    LIMIT 3
) sub
ON u.uni = sub.uni;
