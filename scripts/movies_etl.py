# encoding=utf8
import os, csv


class MoviesEtl(object):

    def __init__(self):
        pass

    def columnar_movies(self, _dataset):
        fh = FileHandler()
        return fh.get_dataset_in_columns(fh.get_doc_data(_dataset))

    def matrix_movies(self, _dataset):
        fh = FileHandler()
        return fh.get_data_matrix(fh.get_doc_data(_dataset))

    @staticmethod
    def color_nocolor_movies(_dataset):
        """
        Get the amount of Colored and Black and White movies for a given dataset
        :param _dataset : defined as path
        """
        bw = 0
        colored = 0
        fh = FileHandler()
        movies_dataset = fh.get_doc_data(_dataset)
        color_types = fh.get_column(0, movies_dataset)
        for c in color_types:
            if c == ' Black and White':
                bw += 1
            if c == 'Color':
                colored += 1
        return bw, colored


class FileHandler(object):

    def __init__(self):
        pass

    @staticmethod
    def get_doc_data(_dataset):
        return open(_dataset, 'r', encoding="utf8")


    @staticmethod
    def get_dataset_in_columns(_dataset):
        column = {}
        reader = csv.reader(_dataset, delimiter=',', quotechar='|')
        headers = next(reader)
        for h in headers:
            column[h] = []
        for row in reader:
            for h, v in zip(headers, row):
                column[h].append(v)
        return column

    @staticmethod
    def get_column(column, _dataset):
        result = []
        spam_reader = csv.reader(_dataset, delimiter=',', quotechar='|')
        for row in spam_reader:
            result.append(row[column])
        return result

    def get_data_matrix(self, _dataset):
        spamreader = csv.reader(_dataset, delimiter=',')
        list_of_list = []
        data = list(list(rec) for rec in spamreader) # reads csv into a list of lists
        for row in data:
            list_of_list.append(list(row))
        return list_of_list
