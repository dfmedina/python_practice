import os, html

from scripts.movies_etl import MoviesEtl

_dir = os.path.dirname(__file__)
_dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')


def main_process():
    m = MoviesEtl(_dataset)
    film_matrix = m.matrix_movies()
    # generate 



if __name__ == '__main__':
    main_process()


