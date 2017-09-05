import os
import logging
import sys
import datetime
import optparse


from lib.movies_etl import MoviesEtl
from lib.output_generator import HtmlGenerator
from lib.query_time import timed

_dir = os.path.dirname(__file__)
_template = os.path.join(_dir, 'template/template.html')

_output = os.path.join(_dir, 'output/output.html')
_output_d = os.path.join(_dir, 'output/d_output.html')

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


@timed
def main_process(output, in_file):
    # TODO: add other types of outputs
    _dataset = os.path.join(_dir, in_file)
    logging.getLogger().debug(in_file)
    logger.debug('Begin processing at: {0}'.format(datetime.datetime.now()))
    m = MoviesEtl(_dataset)

    long_queries = [("Tags Cloud", m.generate_tag_cloud, ["Tag", "Appearance"]),
                    ("Movies per director", m.get_count_movies_per_director, ["Director", "Movies"]),
                    ("Actors ranking by amount of movies", m.get_actor_ranking_by_movies, ["Actor", "Movies",
                                                                                           "Influence", "Best Movie"]),
                    ("Actors ranking by movies and popularity", m.get_actor_ranking_by_movies_and_influence,
                     ["Actor", "Movies", "Influence", "Best Movie"]),
                    ("Genre grossed most per year", m.get_genre_grossed_most_per_year, ["Year", "Genre"]),
                    ("Genre grossed less per year", m.get_genre_grossed_less_per_year, ["Year", "Genre"])
                    ]

    queries = [("Movies in Color - Black and White", m.get_color_nocolor_movies, ["Color Movies",
                                                                                  "Black and White movies"]),
               ("Top 10 best movies", m.get_top_10_movies, ["Movie", "Facebook_likes"]),
               ("Top 20 longest movies", m.get_top_20_longest_movies, ["Movies", "Duration"]),
               ("Top 5 movies grossed most", m.get_top_5_grossed_most_movies, ["Movies", "Gross"]),
               ("Top 5 movies grossed least", m.get_top_5_grossed_less_movies, ["Movies", "Gross"]),
               ("Top 3 most expensive movies", m.get_top_3_most_expensive_movies, ["Movies", "Budget"]),
               ("Top 3 least expensive movies", m.get_top_3_less_expensive_movies, ["Movies", "Budget"]),
               ("Year with more movies", m.get_year_with_most_movies, ["Year", "Movies"]),
               ("Year with least movies", m.get_year_with_less_movies, ["Year", "Movies"]),
               ("Most popular genre", m.get_most_liked_genre, ["Genre", "Likes"]),
               ("Top 3 directors with most reputation", m.get_top_3_directors_reputation, ["Director", "Reputation"])
               ]
    if output == 'html':
        gen = HtmlGenerator()
        gen.generate(queries, _template, _output)
        gen.generate(long_queries, _template, _output_d)
    logger.debug('End processing at: {0}'.format(datetime.datetime.now()))

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', action="store", dest="in_file",
                      help="input csv movies file", default="dataset/movie_metadata.csv")
    parser.add_option('-o', '--output', action="store", dest="output",
                      help="output format definition", default="html")
    options, args = parser.parse_args()
    main_process(options.output, options.in_file)
