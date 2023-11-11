-- only shows named scores

SELECT score, name FROM second_table where name IS NOT NULL AND name != "" ORDER BY score DESC
