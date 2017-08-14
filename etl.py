import os, html

from lib.movies_etl import MoviesEtl

_dir = os.path.dirname(__file__)
_dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')


def main_process():
    m = MoviesEtl(_dataset)
    film_matrix = m.matrix_movies()
    # todo: load csv in list of lists : check
    # todo: get header dict and remove header from list of lists
    # todo: clean and cast to int or numeric: check
    # todo: implement the calculation of execution time





if __name__ == '__main__':
    main_process()


