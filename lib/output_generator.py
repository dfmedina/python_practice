

class HtmlGenerator(object):

    def list_to_table(self, columns, query_result, elapsed):
        header_string = '<table><tr><td> Elapsed Time: {0:.3f}  seconds</td></tr><tr>'.format(elapsed)
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
        table_end = "</table>"
        return header_string + result + table_end

    @staticmethod
    def generate_html(_template, html_result, _output):
        fi = open(_template, 'r')
        filedata = fi.read()
        fi.close()

        html_total = filedata.replace("${table}", html_result)

        fo = open(_output, 'w')
        fo.write(html_total)
        fo.close()

