# encoding=utf8

import unittest
import os
import scripts.mcons as mcons

from scripts.movies_etl import MoviesEtl


class TestMoviesEtl(unittest.TestCase):

    _dir = os.path.dirname(__file__)
    _dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')
    m = MoviesEtl()
    # c_movies = m.columnar_movies(_dataset)
    film_matrix = m.matrix_movies(_dataset)

    def test_color_nocolor_movies(self):
        c, bw = self.m.get_color_nocolor_movies(self.film_matrix)
        print('Colored films:', c)
        print('Black and White films:', bw)

    def test_amount_movies_per_director(self):
        res_directors = self.m.get_movies_per_director(self.film_matrix)
        for dire in res_directors:
            print(dire, res_directors[dire])

    def test_top_10_movies(self):
        c = 0
        movies = self.m.get_top_10_movies(self.film_matrix)
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_top_20_longest_movies(self):
        c = 0
        movies = self.m.get_top_20_longest_movies(self.film_matrix)
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_5_grossed_most_movies(self):
        c = 0
        movies = self.m.get_top_5_grossed_most_movies(self.film_matrix)
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_5_grossed_less_movies(self):
        c = 0
        movies = self.m.get_5_grossed_less_movies(self.film_matrix)
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_3_most_expensive_movies(self):
        c = 0
        movies = self.m.get_3_most_expensive_movies(self.film_matrix)
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_3_less_expensive_movies(self):
        c = 0
        movies = self.m.get_3_less_expensive_movies(self.film_matrix)
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_year_with_most_movies(self):
        print(self.m.get_year_with_most_movies(self.film_matrix))

    def test_year_with_less_movies(self):
        print(self.m.get_year_with_less_movies(self.film_matrix))

    def test_actors_ranking(self):
        all_2_actors = [(movie[6], movie[11].replace('\xa0', '')) for movie in self.film_matrix
                        if movie[6] != '' and movie[6] != 'actor_2_name']
        all_1_actors = [(movie[10], movie[11].replace('\xa0', '')) for movie in self.film_matrix
                        if movie[10] != '' and movie[10] != 'actor_1_name']
        all_3_actors = [(movie[14], movie[11].replace('\xa0', '')) for movie in self.film_matrix
                        if movie[14] != '' and movie[14] != 'actor_3_name']
        all = all_1_actors + all_2_actors + all_3_actors
        for a in all:
            if a[0] == 'Christian Bale':
                print(a)

if __name__ == 'main':
    unittest.main()
