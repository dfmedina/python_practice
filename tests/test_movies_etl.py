# encoding=utf8
import unittest
import os
import lib.mcons as mcons
import logging
import sys
import array

from lib.query_time import timed

from lib.movies_etl import (MoviesEtl, FileHandler)

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestMoviesEtl(unittest.TestCase):

    _dir = os.path.dirname(__file__)
    _dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')
    m = MoviesEtl(_dataset)
    # c_movies = m.columnar_movies(_dataset)
    film_matrix = m.movies

    def test_eval(self):
        l = ['Color', 'James Cameron', '723', '17.8', '-1', '-5.3']
        logging.getLogger().debug(str([FileHandler.cast(val) for val in l]))

    def test_not_duplicates_movie_titles(self):
        all_movie_titles = self.m.get_column(mcons.movie_title)
        for movie in all_movie_titles:
            count = all_movie_titles.count(movie)
            if not count:
                logging.getLogger().debug(str(movie, count))

    def test_movies_loaded(self):
        logging.getLogger().debug(self.film_matrix[0])
        logging.getLogger().debug(self.m.matrix_width)
        logging.getLogger().debug(self.m.matrix_height)

    def test_get_all_actors(self):
        logging.getLogger().debug(self.m.get_actors())

    def test_get_movie(self):
        result = []
        for movie in self.film_matrix:
            if movie[mcons.movie_title] == 'Casino Royale':
                result.append(movie)
        logger.debug(str(result))

    def test_1_color_nocolor_movies(self):
        colors = self.m.get_color_nocolor_movies()
        colored = colors[0][0]
        black_white = colors[0][1]
        logging.getLogger().debug('Colored films: ' + str(colored))
        logging.getLogger().debug('Black and White films: ' + str(black_white))

    def test_2_amount_movies_per_director(self):
        logging.getLogger().debug(self.m.get_count_movies_per_director())

    def test_3_top_10_movies(self):
        c = 0
        movies = self.m.get_top_10_movies()
        for m in movies:
            c += 1
            logging.getLogger().debug(c, '-', m, movies[m])

    def test_4_top_20_longest_movies(self):
        c = 0
        movies = self.m.get_top_20_longest_movies()
        for m in movies:
            c += 1
            logging.getLogger().debug(c, '-', m, movies[m])

    def test_5_top_5_grossed_most_movies(self):
        c = 0
        movies = self.m.get_top_5_grossed_most_movies()
        for m in movies:
            c += 1
            logging.getLogger().debug(c, '-', m, movies[m])

    def test_6_top_5_grossed_less_movies(self):
        c = 0
        movies = self.m.get_top_5_grossed_less_movies()
        for m in movies:
            c += 1
            logging.getLogger().debug(c, '-', m, movies[m])

    def test_7_top_3_most_expensive_movies(self):
        c = 0
        movies = self.m.get_top_3_most_expensive_movies()
        for m in movies:
            c += 1
            logging.getLogger().debug(c, '-', m, movies[m])

    def test_8_top_3_less_expensive_movies(self):
        c = 0
        movies = self.m.get_top_3_less_expensive_movies()
        for m in movies:
            c += 1
            logging.getLogger().debug(c, '-', m, movies[m])

    def test_9_year_with_most_movies(self):
        logging.getLogger().debug(self.m.get_year_with_most_movies())

    def test_10_year_with_less_movies(self):
        logging.getLogger().debug(self.m.get_year_with_less_movies())

    @timed
    def test_11_actor_ranking_by_movies(self):
        logging.getLogger().debug(self.m.get_actor_ranking_by_movies())
        # logging.getLogger().debug(self.m.get_actors_ranking())
        # result = list(filter(lambda movie: actor in (movie[mcons.actor_1_name],
        # movie[mcons.actor_2_name], movie[mcons.actor_3_name]), self.film_matrix))
        #for actor in self.m.get_actors():
        #    self.m.get_actor_movies(actor)

    def test_12_tag_cloud(self):
        logging.getLogger().debug(self.m.generate_tag_cloud())

    def test_13_get_genres(self):
        grossed_most = True
        logging.getLogger().debug(self.m.get_grossed_genre_per_year(grossed_most))

    def test_14_genre_less_profits(self):
        grossed_less = False
        logging.getLogger().debug(self.m.get_grossed_genre_per_year(grossed_less))

    def test_15_actor_ranking_by_movies_and_influence(self):
        logging.getLogger().debug(self.m.get_actor_ranking_by_movies_and_influence())

    def test_16_genre_most_liked(self):
        logging.getLogger().debug(self.m.get_most_liked_genre())

    def test_17_top_3_directors_best_reputation(self):
        logging.getLogger().debug(self.m.get_top_3_directors_reputation())

    def test_decode(self):
        stacktrace = [1, 2, 3, 4, 5]
        logging.getLogger().debug((array.array('B', stacktrace).tostring()))


if __name__ == 'main':
    unittest.main()
