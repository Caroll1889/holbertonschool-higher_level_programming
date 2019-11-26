-- lists all cities contained in a database
SELECT states.id, cities.id
FROM states
INNER JOIN cities
ON states.id=cities.id
ORDER BY states.id
