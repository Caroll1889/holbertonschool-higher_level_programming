-- lists all cities contained in a database
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id=cities.id
ORDER BY cities.id
