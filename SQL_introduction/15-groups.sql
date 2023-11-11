-- create a group by score that shows number of same scores

SELECT score, count(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC
