# encoding=utf8

import unittest
import os

from scripts.movies_etl import MoviesEtl


class TestMoviesEtl(unittest.TestCase):

    _dir = os.path.dirname(__file__)
    _dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')
    m = MoviesEtl()
    c_movies = m.columnar_movies(_dataset)

    def test_color_nocolor_movies(self):
        cm = self.c_movies['color'].count('Color')
        bwm = self.c_movies['color'].count(' Black and White')

    def test_amount_movies_per_director(self):
        ds = self.c_movies['director_name']
        all_directors = set(ds)
        for d in all_directors:
            print('\n')
            print('The director ' + d + ' directed ' + str(ds.count(d)) + ' movies.')
            print('\n')

    def test_10_movies_lest_criticized(self):
        m_indexes = []
        m = (self.c_movies['num_critic_for_reviews'])
        movie_critics = [x for x in (self.c_movies['num_critic_for_reviews']) if x != '']
        movie_critics = list(map(int, movie_critics))
        ten_most_criticized = (sorted(movie_critics, reverse=True)[:10])
        for mov in ten_most_criticized:
            m_indexes.append(m.index(str(mov)))
            print(mov)
        for mi in m_indexes:
            print(self.c_movies['movie_title'][mi])

    def test_20_longest_movies(self):
        print(self.c_movies['movie_title'][750])
        pass


if __name__ == 'main':
    unittest.main()
