# encoding=utf8

import unittest
import os

from scripts.movies_etl import MoviesEtl


class TestMoviesEtl(unittest.TestCase):

    _dir = os.path.dirname(__file__)
    _dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')
    m = MoviesEtl()
    # c_movies = m.columnar_movies(_dataset)
    film_matrix = m.matrix_movies(_dataset)

    def test_color_nocolor_movies(self):
        colored_films = 0
        bw_films = 0
        for film in self.film_matrix:
            if film[0] == 'Color':
                colored_films += 1
            elif film[0] == ' Black and White':
                bw_films += 1
        print('Colored films: ' + str(colored_films))
        print('Black and White films: ' + str(bw_films))

    def test_amount_movies_per_director(self):
        ds = [director[1] for director in self.film_matrix if director[1] != '' and director[1] != 'director_name']
        directors = set(ds)
        for dire in directors:
            print('\n')
            print('Director ' + dire + ' directed ' + str(ds.count(dire))+' films')

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
        print(self.film_matrix[1])


if __name__ == 'main':
    unittest.main()
