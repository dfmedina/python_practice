import os, csv

class MoviesEtl(object):

    def __init__(self):
        pass

    def color_nocolor_movies(self, _dataset):
        with open(_dataset, 'r') as csv_movies:
            spam_reader = csv.reader(csv_movies, delimiter=',', quotechar='|')
            for row in spam_reader:
                print(row[0])
        pass


class FileHandler(object):

    def __init__(self):
        pass
