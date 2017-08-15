import os
import logging
import sys
import time
import optparse

from lib.movies_etl import MoviesEtl
from lib.output_generator import HtmlGenerator
from lib.query_time import QueryTime as timer

_dir = os.path.dirname(__file__)
_dataset = os.path.join(_dir, 'dataset\\movie_metadata.csv')
_template = os.path.join(_dir, 'template.html')


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


def main_process(output):
    # TODO: add other types of outputs
    if output == 'html':
        pass
    logging.getLogger().debug('Begin processing')
    m = MoviesEtl(_dataset)

    # Black and White / Color - total movies
    bwc_query_result, bwc_elapsed = timer.get_query_time(m.get_color_nocolor_movies)
    html_bwc_result = HtmlGenerator().color_movies(bwc_query_result, bwc_elapsed)
    print(html_bwc_result)

    # Movies per director
    mpd_query_result, mpd_elapsed = timer.get_query_time(m.get_count_movies_per_director)
    html_mpd_result = HtmlGenerator().two_columns_table(["director, movies"], mpd_query_result, mpd_elapsed)
    print(html_mpd_result)

    # Top 10 movies
    t10_query_result, t10_elapsed = timer.get_query_time(m.get_top_10_movies)
    t10_result = HtmlGenerator().two_columns_table(["movies", "facebook_likes"], t10_query_result, t10_elapsed)
    print(t10_result)

    # Top 20 longest movies
    t20_query_result, t20_elapsed = timer.get_query_time(m.get_top_20_longest_movies)
    t20_result = HtmlGenerator().two_columns_table(["movies", "duration"], t20_query_result, t20_elapsed)
    print(t20_result)

    '''
    logging.getLogger().debug(timer.get_query_time(m.get_color_nocolor_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_count_movies_per_director))
    logging.getLogger().debug(timer.get_query_time(m.get_top_10_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_top_20_longest_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_top_5_grossed_most_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_top_5_grossed_less_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_top_3_most_expensive_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_top_3_less_expensive_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_year_with_most_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_year_with_less_movies))
    logging.getLogger().debug(timer.get_query_time(m.get_actor_ranking_by_movies))
    logging.getLogger().debug(timer.get_query_time(m.generate_tag_cloud))
    logging.getLogger().debug(timer.get_query_time(m.get_genre_grossed_most_per_year))
    logging.getLogger().debug(timer.get_query_time(m.get_genre_grossed_less_per_year))
    logging.getLogger().debug(timer.get_query_time(m.get_most_liked_genre))
    logging.getLogger().debug(timer.get_query_time(m.get_top_3_directors_reputation))
    '''

if __name__ == '__main__':

    parser = optparse.OptionParser()

    parser.add_option('-o', '--output',
                      action="store", dest="output",
                      help="output format definition", default="html")

    options, args = parser.parse_args()

    main_process(options.output)



