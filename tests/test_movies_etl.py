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
        bwc_films = [film[0] for film in self.film_matrix if film[0] != '' and film[0] != 'color']
        print('Colored films: ' + str(bwc_films.count('Color')))
        print('Black and White films: ' + str(bwc_films.count(' Black and White')))

    def test_amount_movies_per_director(self):
        ds = [director[1] for director in self.film_matrix if director[1] != '' and director[1] != 'director_name']
        directors = set(ds)
        for dire in directors:
            print('\n')
            print('Director ' + dire + ' directed ' + str(ds.count(dire))+' films')

    def test_10_movies_lest_criticized(self):
        movie_critics = [(int(movie[2]), movie[11].replace('\xa0', '')) for movie in self.film_matrix
                         if movie[2] != '' and movie[2] != 'num_critic_for_reviews']
        # movie_critics = sorted(movie_critics, key=lambda x: x[0], reverse=True)[:10]
        #  lambda not necessary since it sorts for the first element of the tuple
        movie_critics = sorted(set(movie_critics), reverse=True)[:10]
        for m in movie_critics:
            print(m[1])

    def test_20_longest_movies(self):
        movie_durations = [(int(movie[3]), movie[11].replace('\xa0', '')) for movie in self.film_matrix
                           if movie[3] != '' and movie[3] != 'duration']
        movie_durations = sorted(set(movie_durations), reverse=True)[:20]
        for m in movie_durations:
            print(m[1])

    def test_5_grossed_most_movies(self):
        movie_gross = [(int(movie[8]), movie[11].replace('\xa0', '')) for movie in self.film_matrix
                       if movie[8] != '' and movie[8] != 'gross']
        movie_gross = sorted(set(movie_gross), reverse=True)[:5]
        for m in movie_gross:
            print(m[1])

    def test_5_grossed_less_movies(self):
        movie_gross = [(int(movie[8]), movie[11].replace('\xa0', '')) for movie in self.film_matrix
                       if movie[8] != '' and movie[8] != 'gross']
        movie_gross = sorted(set(movie_gross))[:5]
        for m in movie_gross:
            print(m[1])

    def test_3_most_expensive_movies(self):
        movie_budget = [(int(movie[22]), movie[11].replace('\xa0', '')) for movie in self.film_matrix
                        if movie[22] != '' and movie[22] != 'budget']
        movie_budget = sorted(set(movie_budget), reverse=True)[:3]
        for m in movie_budget:
            print(m[1])

    def test_3_less_expensive_movies(self):
        movie_budget = [(int(movie[22]), movie[11].replace('\xa0', '')) for movie in self.film_matrix
                        if movie[22] != '' and movie[22] != 'budget']
        movie_budget = sorted(set(movie_budget))[:3]
        for m in movie_budget:
            print(m[1])

    def test_year_with_most_movies(self):
        ys = [year[23] for year in self.film_matrix if year[23] != '' and year[23] != 'title_year']
        print(max(set(ys), key=ys.count))

    def test_year_with_less_movies(self):
        ys = [year[23] for year in self.film_matrix if year[23] != '' and year[23] != 'title_year']
        print(min(set(ys), key=ys.count))

if __name__ == 'main':
    unittest.main()
