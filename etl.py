import os
import logging
import sys

from lib.movies_etl import MoviesEtl
from lib.output_generator import HtmlGenerator

_dir = os.path.dirname(__file__)
_dataset = os.path.join(_dir, 'dataset\\movie_metadata.csv')


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


def main_process():
    m = MoviesEtl(_dataset)
    queries = [m.get_color_nocolor_movies, m.get_count_movies_per_director]
    HtmlGenerator.generate_html(queries)
    logging.getLogger().debug(m.get_color_nocolor_movies())
    logging.getLogger().debug(m.get_count_movies_per_director())
    logging.getLogger().debug(m.get_top_10_movies())
    logging.getLogger().debug(m.get_top_20_longest_movies())
    logging.getLogger().debug(m.get_top_5_grossed_most_movies())
    logging.getLogger().debug(m.get_top_5_grossed_less_movies())
    logging.getLogger().debug(m.get_top_3_most_expensive_movies())
    logging.getLogger().debug(m.get_top_3_less_expensive_movies())
    logging.getLogger().debug(m.get_year_with_most_movies())
    logging.getLogger().debug(m.get_year_with_less_movies())
    logging.getLogger().debug(m.get_actor_ranking_by_movies())
    logging.getLogger().debug(m.generate_tag_cloud())
    logging.getLogger().debug(m.get_grossed_genre_per_year(True))
    logging.getLogger().debug(m.get_grossed_genre_per_year(False))
    logging.getLogger().debug(m.get_most_liked_genre())
    logging.getLogger().debug(m.get_top_3_directors_reputation())

if __name__ == '__main__':
    main_process()


