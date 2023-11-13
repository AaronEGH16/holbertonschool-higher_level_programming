-- shows all the genres of the show Dexter (through the connection by id with the tv_show_genres table)

USE hbtn_0d_tvshows;
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
