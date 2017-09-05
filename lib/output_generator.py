import sys
import logging
from lib.query_time import QueryTime as Timer

logger = logging.getLogger()
logger.level = logging.DEBUG


class HtmlGenerator(object):

    def list_to_table(self, columns, query_result, elapsed):
        def is_dup(tup):
            return len(tup) == 2

        header_string = '<table align="center"><tr><td> Elapsed Time: {0:.3f}  seconds</td></tr><tr>'.format(elapsed)
        for item in columns:
            header_string += "<td>"+item+"</td>"
        header_string += "</tr>"
        result = ''
        if isinstance(query_result, dict):
            for res in query_result:
                result += '<tr><td>'+str(res)+'</td><td>'+str(query_result[res])+'</td></tr>'
        else:
            for res in query_result:
                result += '<tr>'
                for i in range(len(res)):
                    result += '<td>'+str(res[i])+'</td>'
                result += '</tr>'
        table_end = "</table>"
        return header_string + result + table_end

    @staticmethod
    def generate_html(_template, html_result, _output):
        file_data = ''
        try:
            fi = open(_template, 'r')
            file_data = fi.read()
            fi.close()
        except IOError:
            logging.getLogger().debug(IOError.strerror)

        html_total = file_data.replace("${table}", html_result)

        fo = open(_output, 'w+')
        fo.write(html_total)
        fo.close()

    def generate(self, queries, _template, _output):
        html_result = ''
        for query in queries:
            html_result += "<h3>{0}</h3>".format(query[0])
            q_result, elapsed = Timer.get_query_time(query[1])
            html_result += self.list_to_table(query[2], q_result, elapsed)
        HtmlGenerator.generate_html(_template, html_result, _output)

    # TODO: generate tag cloud for html instead of showing the cloud as table
    def generate_tag_cloud(self, tag_cloud):
        for tag in tag_cloud:
            pass



