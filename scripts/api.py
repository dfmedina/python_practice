import os

from scripts.movies_etl import MoviesEtl

_dir = os.path.dirname(__file__)
_dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')


if __name__ == '__main__':
    m = MoviesEtl()
    # c_movies = m.columnar_movies(_dataset)
    film_matrix = m.matrix_movies(_dataset)

