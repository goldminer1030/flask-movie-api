import psycopg2

conn = psycopg2.connect("host=localhost dbname=flskmovies_db user=flskmovies password=greenpeace2018")
cur = conn.cursor()
# cur.execute("""
# CREATE TABLE movies(
# movie_title text,
# id integer PRIMARY KEY,
# recommended_movie_id_0 text,
# recommended_movie_id_1 text,
# recommended_movie_id_2 text,
# recommended_movie_id_3 text,
# recommended_movie_id_4 text,
# recommended_movie_title_0 text,
# recommended_movie_title_1 text,
# recommended_movie_title_2 text,
# recommended_movie_title_3 text,
# recommended_movie_title_4 text
# )
# """)


with open('database_.csv', 'r') as f:
    cmd = "COPY movies(movie_title, id, recommended_movie_id_0, recommended_movie_id_1, recommended_movie_id_2, " + \
          "recommended_movie_id_3, recommended_movie_id_4, recommended_movie_title_0, recommended_movie_title_1, " \
          "recommended_movie_title_2, recommended_movie_title_3, recommended_movie_title_4) " \
          "FROM STDIN WITH (FORMAT CSV, HEADER FALSE)"
    # cur.copy_expert(cmd, f)
    cur.copy_from(f, 'movies', sep='\t')

conn.commit()
