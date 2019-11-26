-- tv shows
SELECT tv_shows.tittle, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show.id=tv_show_genres.show_id
ORDER BY tv_shows.tittle, tv_show_genres.genre_id
