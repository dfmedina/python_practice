import os


class HtmlGenerator(object):

    def __init__(self):
        _dir = os.path.dirname(__file__)
        self.template = os.path.join(_dir, '..\\output.html')

    def import_template(self):
        open(self.template)

    def html_single_value(self, value):
        return ''

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
