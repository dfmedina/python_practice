# encoding=utf8
import numpy
import unittest
import os
import lib.mcons as mcons

from lib.movies_etl import (MoviesEtl, FileHandler)


class TestMoviesEtl(unittest.TestCase):

    _dir = os.path.dirname(__file__)
    _dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')
    m = MoviesEtl(_dataset)
    # c_movies = m.columnar_movies(_dataset)
    film_matrix = m.movies

    def test_eval(self):
        l = ['Color', 'James Cameron', '723', '17.8', '-1', '-5.3']
        print([FileHandler.cast(val) for val in l])

    def test_not_duplicates_movie_titles(self):
        all_movie_titles = self.m.get_column(mcons.movie_title)
        for movie in all_movie_titles:
            count = all_movie_titles.count(movie)
            if count > 1:
                print(movie, count)

    def test_movies_loaded(self):
        print(self.film_matrix[0])
        print(self.m.matrix_width)
        print(self.m.matrix_height)

    def test_get_all_actors(self):
        print(self.m.get_actors())

    def test_get_movie(self):
        result = []
        for movie in self.film_matrix:
            if movie[mcons.movie_title] == 'Casino Royale':
                result.append(movie)
        print(result)

    def test_1_color_nocolor_movies(self):
        c, bw = self.m.get_color_nocolor_movies()
        print('Colored films:', c)
        print('Black and White films:', bw)

    def test_2_amount_movies_per_director(self):
        print(self.m.get_count_movies_per_director())

    def test_3_top_10_movies(self):
        c = 0
        movies = self.m.get_top_10_movies()
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_4_top_20_longest_movies(self):
        c = 0
        movies = self.m.get_top_20_longest_movies()
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_5_top_5_grossed_most_movies(self):
        c = 0
        movies = self.m.get_top_5_grossed_most_movies()
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_6_top_5_grossed_less_movies(self):
        c = 0
        movies = self.m.get_5_grossed_less_movies()
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_7_top_3_most_expensive_movies(self):
        c = 0
        movies = self.m.get_3_most_expensive_movies()
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_8_top_3_less_expensive_movies(self):
        c = 0
        movies = self.m.get_3_less_expensive_movies()
        for m in movies:
            c += 1
            print(c, '-', m, movies[m])

    def test_9_year_with_most_movies(self):
        print(self.m.get_year_with_most_movies())

    def test_10_year_with_less_movies(self):
        print(self.m.get_year_with_less_movies())

    def test_11_actor_ranking_by_movies(self):
        print(self.m.get_actor_ranking_by_movies())

    def test_12_tag_cloud(self):
        print(self.m.generate_tag_cloud())

    def test_13_get_genres(self):
        grossed_most = True
        print(self.m.get_grossed_genre_per_year(grossed_most))

    def test_14_genre_less_profits(self):
        grossed_less = False
        print(self.m.get_grossed_genre_per_year(grossed_less))

    def test_15_actor_ranking_by_movies_and_influence(self):
        print(self.m.get_actor_ranking_by_movies_and_influence())

    def test_16_genre_most_liked(self):
        print(self.m.get_most_liked_genre())

    def test_17_top_3_directors_best_reputation(self):
        print(self.m.get_top_3_directors_reputation())


if __name__ == 'main':
    unittest.main()
