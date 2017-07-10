# encoding=utf8

import unittest
import os


from scripts.movies_etl import MoviesEtl
import logging


class TestMoviesEtl(unittest.TestCase):

    _dir = os.path.dirname(__file__)
    _dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')

    def test_color_nocolor_movies(self):
        movies_searcher = MoviesEtl()
        a, b = movies_searcher.color_nocolor_movies(self._dataset)
        print("Black and White movies: ", a)
        print("Colored movies: ", b)
        pass

if __name__ == 'main':
    unittest.main()