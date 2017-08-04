# encoding=utf8
import os, csv
import scripts.mcons as mcons


class MoviesEtl(object):

    def __init__(self):
        pass

    @staticmethod
    def get_list_context(context, elements):
        return [elem[context] for elem in elements if elem[context] != '']

    @staticmethod
    def get_pairs_context(context1, context2, elements):
        return [(int(movie[context1]), movie[context2].replace('\xa0', '')) for movie in elements
                if movie[context1] != '' and movie[context2] != '']

    @staticmethod
    def matrix_movies(_dataset):
        fh = FileHandler()
        return fh.get_data_matrix(fh.get_doc_data(_dataset))

    def get_top_n_movies(self, cond, n, m_list, ord=True):
        r_dic = {}
        in_list = sorted(self.get_pairs_context(cond, mcons.movie_title, m_list),
                         reverse=ord)[:n]
        for elem in in_list:
            r_dic[elem[1]] = elem[0]
        return r_dic

    def get_color_nocolor_movies(self, films):
        c = 'Color'
        bw = ' Black and White'
        bwc_films = self.get_list_context(mcons.color, films)
        return bwc_films.count(c), bwc_films.count(bw)

    def get_movies_per_director(self, films):
        dir_movies = {}
        ds = self.get_list_context(mcons.director_name, films)
        directors = set(ds)
        for dire in directors:
            dir_movies[dire] = ds.count(dire)
        return dir_movies

    def get_top_10_movies(self, films):
        return self. get_top_n_movies(mcons.num_critic_for_reviews, 11, films)

    def get_top_20_longest_movies(self, films):
        return self. get_top_n_movies(mcons.duration, 20, films)

    def get_top_5_grossed_most_movies(self, films):
        return self.get_top_n_movies(mcons.gross, 6, films)

    def get_5_grossed_less_movies(self, films):
        return self.get_top_n_movies(mcons.gross, 6, films, ord=False)

    def get_3_most_expensive_movies(self, films):
        return self.get_top_n_movies(mcons.budget, 3, films)

    def get_3_less_expensive_movies(self, films):
        return self.get_top_n_movies(mcons.budget, 3, films, ord=False)

    def get_year_with_most_movies(self, films):
        ym = self.get_list_context(mcons.title_year, films)
        return max(set(ym), key=ym.count)

    def get_year_with_less_movies(self, films):
        ym = self.get_list_context(mcons.title_year, films)
        return min(set(ym), key=ym.count)


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
