
-- List a join of two tables

SELECT cities.id, cities.name, states.name FROM cities JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
