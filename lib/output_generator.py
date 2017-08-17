import os


class HtmlGenerator(object):

    def __init__(self):
        _dir = os.path.dirname(__file__)
        self.template = os.path.join(_dir, '..\\template\\template.html')

    def html_table(self, data):
        row_length = len(data)
        print('<table>')
        counter = 0
        for element in data:
            if counter % row_length == 0:
                print('<tr>')
            print('<td>%s</td>' % element)
            counter += 1
            if counter % row_length == 0:
                print('</tr>')
        if counter % row_length != 0:
            for i in range(0, row_length - counter % row_length):
                print('<td>&nbsp;</td>')
            print('</tr>')
        print('</table>')

    @staticmethod
    def color_movies(tup, elapsed):
        return "<a> Color movies: {0}, Black and White movies: {1} -- elapsed time: {2}  seconds</a>"\
            .format(str(tup[0]), str(tup[1]), elapsed)

    def list_to_table(self, columns, query_result, elapsed):
        header_string = '<table><tr>'
        for item in columns:
            header_string += "<td>"+item+"</td>"
        header_string += "</tr>"
        result = ''
        if isinstance(query_result, dict):
            for res in query_result:
                result += '<tr><td>'+str(res)+'</td><td>'+str(query_result[res])+'</td></tr>'
        else:
            for res in query_result:
                result += '<tr><td>' + str(res[0]) + '</td><td>' + str(res[1]) + '</td></tr>'
        table_end = "<tr><td>Elapsed time: {0} -- seconds</td></tr></table>".format(elapsed)
        return header_string + result + table_end


