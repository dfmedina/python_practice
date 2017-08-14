import csv
import hashlib

from lib import mcons


class FileHandler(object):

    def __init__(self):
        pass

    @staticmethod
    def matrix_height(matrix):
        return len(matrix)

    @staticmethod
    def matrix_width(matrix):
        return len(matrix[0])

    @staticmethod
    def get_doc_data(_dataset):
        return open(_dataset, 'r', encoding="utf8")

    @staticmethod
    def get_html_template(html_file):
        pass

    def get_data_matrix(self, _dataset):
        c_reader = csv.reader(_dataset, delimiter=',')
        next(c_reader, None)  # csv has header
        list_of_list = []
        title_seen = {}
        data = list(list(rec) for rec in c_reader)  # puts csv into a list of lists
        for row in data:
            # row = self.generate_hash(row) -- generate id per row
            row = list([self.cast(elem) for elem in row])  # cast the values from the row to their correct types
            if row[mcons.movie_title] not in title_seen.keys():
                title_seen[row[mcons.movie_title]] = row[mcons.title_year]
                list_of_list.append(row)
        return list_of_list

    @staticmethod
    def cast(val):
        if '\xa0' in val:
            val = val.replace('\xa0', '')
        val = val.rstrip()
        constructors = [int, float, str]
        for c in constructors:
            try:
                return c(val)
            except ValueError:
                pass

    @staticmethod
    def generate_hash(row):
        movie_hash = hashlib.md5((row[mcons.movie_title]).encode('utf-8')).hexdigest()
        row.insert(0, movie_hash)
        return row
