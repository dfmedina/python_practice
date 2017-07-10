# encoding=utf8
import os, csv


class MoviesEtl(object):

    def __init__(self):
        pass

    def color_nocolor_movies(self, _dataset):
        """

        :param _dataset : defined as path
        """
        bw = 0
        colored = 0
        fh = FileHandler()
        color_types = fh.csv_mapper(0, _dataset)
        for c in color_types:
            if c == ' Black and White':
                bw += 1
            if c == 'Color':
                colored += 1
        return bw, colored


class FileHandler(object):

    def __init__(self):
        pass

    def csv_mapper(self, column, _dataset):
        result = []
        with open(_dataset, 'r', encoding="utf8") as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in spam_reader:
                result.append(row[column])
        return result
