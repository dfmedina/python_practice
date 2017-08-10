# encoding=utf8

import unittest
import os
import scripts.mcons as mcons

from scripts.movies_etl import MoviesEtl


class TestMoviesEtl(unittest.TestCase):

    _dir = os.path.dirname(__file__)
    _dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')
    m = MoviesEtl(_dataset)
    # c_movies = m.columnar_movies(_dataset)
    film_matrix = m.matrix_movies()

    def test_color_nocolor_movies(self):
        c, bw = self.m.get_color_nocolor_movies(self.film_matrix)
        print(len(self.film_matrix[5]))
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
        for movie in self.m.get_actor_data(self.film_matrix):
            if movie[0] == 'Christoph Waltz':
                print(movie)

if __name__ == 'main':
    unittest.main()
