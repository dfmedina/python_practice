
class HtmlGenerator(object):

    def __init__(self):
        html_str = """
                    <table border=1>
                         <tr>
                           <th>Number</th>
                           <th>Square</th>
                         </tr>
                         <indent>
                         <% for i in range(10): %>
                           <tr>
                             <td><%= i %></td>
                             <td><%= i**2 %></td>
                           </tr>
                         </indent>
                    </table>
                    """