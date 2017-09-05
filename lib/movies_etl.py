# encoding=utf8

import lib.mcons as mcons
from lib.file_handler import FileHandler


class MoviesEtl(object):

    def __init__(self, _dataset):
        """
        Constructor for MoviesEtl class. This constructor will generate
        the movies matrix from a given csv file and make the matrix an attribute for the class 
        
        :param _dataset: csv file with movies information
        """
        fh = FileHandler()
        doc_data = FileHandler.get_doc_data(_dataset)
        matrix = fh.get_data_matrix(doc_data)
        self.matrix_height = len(matrix)
        self.matrix_width = len(matrix[0])
        self.movies = matrix

    def get_top_n_movies(self, cond, n, order=True, movies=None):
        """
        Generate a dictionary of movies with a given condition as value.
        cond: condition for the filter of the dataset
        n: number to define the top list
        order: value to define if the result will be ordered
        movies: a sub-selection of a list can be passed to generate a top 

        :rtype: top N dictionary with movie title as key and the given condition as value
        ordered by value
        """
        if movies is None:
            movies = self.movies
        r_dic = {}
        in_list = sorted(set(self.get_pairs_context(cond, mcons.movie_title, movies)),
                         reverse=order,
                         key=lambda x: x[0])[:n]
        for elem in in_list:
            r_dic[elem[1]] = elem[0]
        return r_dic

    def get_column(self, column_name):
        """
        return a column of the matrix
        :rtype: list for a given column
        """
        return [elem[column_name] for elem in self.movies if elem[column_name]]

    def get_columns(self, *args):
        merged_columns = []
        for c_name in args:
            merged_columns.extend(self.get_column(c_name))
        return merged_columns

    def get_pairs_context(self, context1, context2, movies=None):
        if movies is None:
            movies = self.movies
        return [(movie[context1], movie[context2]) for movie in movies
                if movie[context1] and movie[context2]]

    def get_actor_movies(self, actor_name):
        actor_movies = []
        for movie in self.movies:
            if movie[mcons.actor_1_name] == actor_name \
                    or movie[mcons.actor_2_name] == actor_name \
                    or movie[mcons.actor_3_name] == actor_name:
                actor_movies.append(movie)
        return actor_movies

    def get_actor_best_movie(self, actor_movies):
        best_movies = list(self.get_top_n_movies(mcons.num_critic_for_reviews, 1, movies=actor_movies).keys())
        if len(best_movies) >= 1:
            return best_movies[0]

    def get_actor_influence(self, actor_name, actor_movies):
        influence = 0
        for movie in actor_movies:
            if movie[mcons.actor_1_name] == actor_name:
                influence += movie[mcons.actor_1_facebook_likes]
            if movie[mcons.actor_2_name] == actor_name:
                influence += movie[mcons.actor_2_facebook_likes]
            if movie[mcons.actor_3_name] == actor_name:
                influence += movie[mcons.actor_3_facebook_likes]
        return influence

    def get_actors(self):
        all_actors = self.get_columns(mcons.actor_1_name, mcons.actor_2_name, mcons.actor_3_name)
        return list(set(all_actors))

    def get_actors_ranking(self):
        actor_ranking = []
        for actor in self.get_actors():
            actor_movies = self.get_actor_movies(actor)
            actor_ranking.append((actor,
                                  len(actor_movies),
                                  self.get_actor_influence(actor, actor_movies),
                                  self.get_actor_best_movie(actor_movies)
                                  ))
        return actor_ranking

    def get_actor_ranking_by_movies(self):
        return sorted(self.get_actors_ranking(), key=lambda x: x[1], reverse=True)

    def get_actor_ranking_by_movies_and_influence(self):
        return sorted(self.get_actors_ranking(), key=lambda x: (x[1], x[2]), reverse=True)

    def get_color_nocolor_movies(self):
        c = 'Color'
        bw = ' Black and White'
        bwc_films = self.get_column(mcons.color)
        return [(bwc_films.count(c), bwc_films.count(bw))]

    def get_directors(self):
        return list(set(self.get_column(mcons.director_name)))

    def get_movies_per_director(self):
        dir_movies = dict()
        ds = self.get_pairs_context(mcons.director_name, mcons.movie_title)
        directors = self.get_directors()
        for dire in directors:
            for movie in ds:
                if movie[0] == dire:
                    if dire not in dir_movies.keys():
                        dir_movies[dire] = [movie[1]]
                    else:
                        dir_movies[dire].append(movie[1])
        return dir_movies

    def get_count_movies_per_director(self):
        count_movies_director = []
        mpd = self.get_movies_per_director()
        for director in mpd:
            count_movies_director.append((director, len(mpd[director])))
        return sorted(count_movies_director, key=lambda x: x[1], reverse=True)

    def get_top_10_movies(self):
        return self.get_top_n_movies(mcons.num_critic_for_reviews, 10)

    def get_top_20_longest_movies(self):
        return self. get_top_n_movies(mcons.duration, 20)

    def get_top_5_grossed_most_movies(self):
        return self.get_top_n_movies(mcons.gross, 5)

    def get_top_5_grossed_less_movies(self):
        return self.get_top_n_movies(mcons.gross, 5, order=False)

    def get_top_3_most_expensive_movies(self):
        return self.get_top_n_movies(mcons.budget, 3)

    def get_top_3_less_expensive_movies(self):
        return self.get_top_n_movies(mcons.budget, 3, order=False)

    def get_year_with_most_movies(self):
        ym = self.get_column(mcons.title_year)
        max_year = max(set(ym), key=ym.count)
        count = ym.count(max_year)
        return [(max_year, count)]

    def get_year_with_less_movies(self):
        ym = self.get_column(mcons.title_year)
        min_year = min(set(ym), key=ym.count)
        count = ym.count(min_year)
        return [(min_year, count)]

    def get_5_best_directors(self):
        self.get_movies_per_director()

    def get_director_movies(self, director):
        d_movies = []
        for movie in self.movies:
            if movie[mcons.director_name] == director:
                d_movies.append(movie)
        return d_movies

    def get_director_reputation(self, director):
        reputation = 0
        director_movies = self.get_director_movies(director)
        for movie in director_movies:
            reputation += movie[mcons.director_facebook_likes]
        return reputation

    def get_all_directors_reputation(self):
        director_rep = []
        directors = self.get_directors()
        for dire in directors:
            director_rep.append((dire, self.get_director_reputation(dire)))
        return director_rep

    def get_top_3_directors_reputation(self):
        return sorted(self.get_all_directors_reputation(), key=lambda x: x[1], reverse=True)[:3]

    def get_movie_genres(self, movie=None):
        if movie is None:
            movie = self.movies
        all_genres = []
        for movie in self.get_column(mcons.genres):
            all_genres.extend(movie.split('|'))
        return list(set(all_genres))

    def get_movie_years(self):
        return list(set(self.get_column(mcons.title_year)))

    def get_grossed_genre_per_year(self, order):
        gen_year_gross = []
        for year in self.get_movie_years():
            gen_year = []
            for gen in self.get_movie_genres():
                total_gross = 0
                for movie in self.movies:
                    if movie[mcons.title_year] == year and gen in movie[mcons.genres]:
                        try:
                            total_gross += movie[mcons.gross]
                        except TypeError:
                            pass
                gen_year.append((gen, total_gross))
            gg = sorted(gen_year, key=lambda x: x[1], reverse=order)[:1]
            gen_year_gross.append((year, gg[0][0]))
        return gen_year_gross

    def get_genre_grossed_most_per_year(self):
        return self.get_grossed_genre_per_year(True)

    def get_genre_grossed_less_per_year(self):
        return self.get_grossed_genre_per_year(False)

    def get_most_liked_genre(self):
        gen_likes = []
        for gen in self.get_movie_genres():
            likes = 0
            for movie in self.movies:
                if gen in movie[mcons.genres]:
                    try:
                        likes += movie[mcons.movie_facebook_likes]
                    except TypeError:
                        pass
            gen_likes.append((gen, likes))
        return sorted(gen_likes, key=lambda x: x[1], reverse=True)[:1]

    def generate_tag_cloud(self):
        tags_counts = []
        tags = []
        for movie in self.movies:
            [tags.append(tag)for tag in movie[mcons.plot_keywords].split('|')]
        all_tags = set(tags)
        for t in all_tags:
            if t:
                tags_counts.append((t, tags.count(t)))
        return sorted(tags_counts, key=lambda x: x[1], reverse=True)

    def get_movies_of_year(self, year):
        return list(filter(lambda x: x[mcons.title_year] == year, self.movies))
