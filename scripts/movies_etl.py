# encoding=utf8
import os, csv
import scripts.mcons as mcons


class MoviesEtl(object):

    def __init__(self):
        pass

    def get_list_context(self, context, elements):
        return [elem[context] for elem in elements if elem[context] != '']

    def get_pairs_context(self, context, elements):
        return [(int(movie[context]), movie[context].replace('\xa0', '')) for movie in elements if movie[2] != '']

    @staticmethod
    def matrix_movies(_dataset):
        fh = FileHandler()
        return fh.get_data_matrix(fh.get_doc_data(_dataset))

    def get_color_nocolor_movies(self, films):
        bwc_films = self.get_list_context(mcons.color, films)
        return bwc_films.count('Color'), bwc_films.count(' Black and White')

    def get_movies_per_director(self, films):
        dir_movies = {}
        ds = self.get_list_context(mcons.director_name, films)
        directors = set(ds)
        for dire in directors:
            dir_movies[dire] = ds.count(dire)
        return dir_movies

    def get_top_10_movies_by_critics(self, films):
        mov_crit = {}
        mc = self.get_pairs_context(mcons.num_critic_for_reviews, films)
        movie_critics = sorted(set(mc), reverse=True)[:10]
        for m in movie_critics:
            mov_crit[m[2]] = m(1)
        return mov_crit

    def get_20_longest_movies(self, films):
        movie_durations = [(int(movie[3]), movie[11].replace('\xa0', '')) for movie in films
                           if movie[3] != '' and movie[3] != 'duration']
        movie_durations = sorted(set(movie_durations), reverse=True)[:20]
        for m in movie_durations:
            print(m[1])


class FileHandler(object):

    def __init__(self):
        pass

    @staticmethod
    def get_doc_data(_dataset):
        return open(_dataset, 'r', encoding="utf8")

    @staticmethod
    def get_data_matrix(_dataset):
        c_reader = csv.reader(_dataset, delimiter=',')
        next(c_reader, None)
        list_of_list = []

        data = list(list(rec) for rec in c_reader)  # puts csv into a list of lists
        for row in data:
            list_of_list.append(list(row))
        return list_of_list


class QueryTime(object):

    def __init__(self):
        pass

    def get_query_time(self, query):
        pass
