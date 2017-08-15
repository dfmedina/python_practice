import os


class HtmlGenerator(object):

    def __init__(self):
        _dir = os.path.dirname(__file__)
        self.template = os.path.join(_dir, 'template.html')

    def generate_html(self, queries):
        with open(self.template, "w") as my_file:
            my_file.write("<html><body><table>")
            for query in queries:
                query_string = "<tr><td>$query</td></tr>"
                query_string = query_string.replace("$query", str(query()))
                my_file.write(query_string)
            my_file.write("</table></body></html>")

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

