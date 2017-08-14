import os, html

from lib.movies_etl import MoviesEtl

_dir = os.path.dirname(__file__)
_dataset = os.path.join(_dir, '..\\dataset\\movie_metadata.csv')


def main_process():
    m = MoviesEtl(_dataset)
    film_matrix = m.movies
    m.get_color_nocolor_movies()
    m.get_count_movies_per_director()
    m.get_top_10_movies()




if __name__ == '__main__':
    main_process()


