"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    on importe le module sys
"""
import sys

""" 
    global variables
"""

def extract_elt(raw):
    """
    """
    elt = {}

    name, properties = raw.split(' = ')
    name = name.strip();
    properties = properties.strip()
    properties.replace(', ', ' ')

    #s= position:1, number:4, small: Be, molar:9.012182, electron:2 2
    elt = dict(item.split(":") for item in properties.split(", "))
    elt['name'] = name

    #print('elt: ', elt)
    return elt

def extract_elements(filename):
    """
    """
    elements_dict = {}
    elements_dict['elements'] = []
    cur_pos = 0

    """ with : il nous assure que le fichier sera ferme """
    with open(filename, 'r') as f:
        for line in f:
            elt = extract_elt(line)
            elt_pos = int(elt['position'])
            if cur_pos == 18:
                cur_pos = 0

            if cur_pos == elt_pos:
                #print('pushing NEW elt  with position: cur_pos ', cur_pos, 'elt_pos', elt_pos, 'elt:', elt)
                elements_dict['elements'].append(elt)
                cur_pos += 1
            
            if cur_pos < elt_pos:
                while cur_pos < int(elt_pos):
                    #print('pushing elt EMPTY {} with position cur_posr:', cur_pos, 'elt_pos:', elt_pos)
                    elements_dict['elements'].append({})
                    cur_pos += 1

                #print('pushing NEW elt with position: cur_pos ', cur_pos, 'elt_pos', elt_pos, 'elt:', elt)
                elements_dict['elements'].append(elt)
                cur_pos += 1
    return elements_dict

def build_html_elt_cell(raw):
    """
    """
    elt = {}

    name, properties = raw.split(' = ')
    name = name.strip();
    properties = properties.strip()
    properties.replace(', ', ' ')

    #s= position:1, number:4, small: Be, molar:9.012182, electron:2 2
    elt = dict(item.split(":") for item in properties.split(", "))
    elt['name'] = name

    print('elt: ', elt)
    return elt

def build_html_table_elts(filename):
    """
    """
    elements_dict = {}
    elements_dict['elements'] = []
    cur_pos = 0

    """ with : il nous assure que le fichier sera ferme """
    with open(filename, 'r') as f:
        for line in f:
            elt = extract_elt(line)
            elt_pos = elt['position']
            if elt_pos != cur_pos:
                for i in range(cur_pos, int(elt_pos)):
                    print('pushing elt {} with position: ',  i)
                    elements_dict['elements'].append({})
            else:
                print('previous pos', pos, "pushing elt with position:", elt_pos)

            elements_dict['elements'].append(elt)
            cur_pos += 1
            cur_pos %= 17

    return elements_dict

def bb():
    d = {'kiwi': ['kiwi.good.svg'], 'apple': ['apple.good.2.svg', 'apple.good.1.svg'], 'banana': ['banana.1.ugly.svg', 'banana.bad.2.svg']}

    html = """<html><table border="1">
    <tr><th>Object</th><th>Good</th><th>Bad</th><th>Ugly</th></tr>"""
    for fruit in d:
        html += "<tr><td>{}</td>".format(fruit)
        for state in "good", "bad", "ugly":
            html += "<td>{}</td>".format('<br>'.join(f for f in d[fruit] if ".{}.".format(state) in f))
        html += "</tr>"
    html += "</table></html>"
    print('html page')
    print(html)

def html_page_header():
    page_header = """<!DOCTYPE html>
<html lang="en">
    <head>
	<meta charset="utf-8">
	<title>Periodic Table</title>
	<style>
            html {
                font-family: sans-serif;
            }

            section { 
                border: double medium; 
                margin: 10px 20px;
                padding: 10px;
            }

            table {
                border-collapse: collapse;
                border-style: solid;
                border-width: 2px;
                border-color: pink;
            }

            /*table td, th {
                border-style: solid;
                border-color: pink;
                border-width: 1px;
                padding: 10px 20px;
            }*/
            td, th {
                padding: 10px 20px;
            }

            th {
                background-color: rgb(190,190,190);
            }

            #selected {
                border: 2px solid #424242!important;
            }

        </style>
    </head>"""
    return page_header

def html_page_body_start():
    page_body_start = """
    <body>
        <header>
            <h1>mendeleev periodic table</h1>
            <p>generated from pyhon sctipt</p>
            <p><small>Piscine Python day00 ex07</small></p>
            <br />
        </header>
    """
    return page_body_start

def html_row_cell(elt):
    #elt:  {'small': ' H', 'electron': '1', 'molar': '1.00794', 'name': 'Hydrogen', 'number': '1', 'position': '0'}
    #print("html_row_cell(): start")
    if not elt:
        row_cell = """
                    <td></td>
        """
    else:
        name = elt['name']
        number = elt['number']
        small = elt['small']
        molar = elt['molar']
        electron = elt['electron']
        row_cell = """
                    <td style="border:1px solid black; padding:10px;">
                        <h4>"""+name+"""</h4>
                        <ul>
                            <li>"""+number+"""</li>
                            <li>"""+small+"""</li>
                            <li>"""+molar+"""</li>
                            <li>"""+electron+""" electron</li>
                        </ul>
                    </td>"""
    #print(row_cell)
    #print("html_row_cell(): end")
    return(row_cell)

def html_one_row(chunk):
    #html_row_cell(elt)
    #print("chunk start")
    #print(chunk)
    one_row = """
                <tr>
    """
    elt_cell = ""
    for x in chunk:
        elt_cell = html_row_cell(x)
        one_row += elt_cell

    one_row += """
                </tr>
    """
    #print(one_row)
    #print("chunk end")
    return one_row

def html_rows(elements_dict):
    data = elements_dict['elements']
    #print('coucoucoucou START')
    #print(elements_dict)
    #print('coucoucoucou END')

    one_row = ""
    table_row = ""
    elts_row = []

    for i in range(0, len(data), 18):
        chunk = data[i:i + 18]
        one_row = html_one_row(chunk)
        table_row += one_row
    #print(table_row)
    #sys.exit(1)
    return table_row

def html_page_body_table(elements_dict):
    page_body_table_start = """
        <table>
            <caption>Mendeleiv table</caption>
            <thead>
                <tr>
                    <th> 0</th>
                    <th> 1</th>
                    <th> 2</th>
                    <th> 3</th>
                    <th> 4</th>
                    <th> 5</th>
                    <th> 6</th>
                    <th> 7</th>
                    <th> 8</th>
                    <th> 9</th>
                    <th>10</th>
                    <th>11</th>
                    <th>12</th>
                    <th>13</th>
                    <th>14</th>
                    <th>15</th>
                    <th>16</th>
                    <th>17</th>
                </tr>
            </thead>
            <tbody>"""

    all_rows = ""
    all_rows = html_rows(elements_dict)
    page_body_table_body = """ {all_rows} """.format(all_rows=all_rows)

    page_body_table_end = """
            </tbody>
        </table>
    """

    page_body_table = page_body_table_start + page_body_table_body + page_body_table_end
    return page_body_table

def html_page_body_end():
    page_body_end = """
    </body>
    """
    return page_body_end

def html_page_body(elements_dict):
    m = html_page_body_start()
    m += html_page_body_table(elements_dict)
    m += html_body_footer()
    m += html_page_body_end()
    return m


def html_body_footer():
    body_footer = """
        <footer>
	        <p>Ceci est le footer</p>
	    </footer>
    """
    return body_footer

def html_page_footer():
    page_footer = """
</html>
    """
    return page_footer


def html_page(elements_dict):
    m = html_page_header()
    m += html_page_body(elements_dict)
    m += html_page_footer()
    return m

def main(args):
    """
    """
    #filename = 'small_periodic_table.txt'
    filename = 'periodic_table.txt'
    if len(sys.argv) != 1:
        print('usage: ./periodic_table.py')
        sys.exit(1)

    elements_dict = extract_elements(filename)
    #print(elements_dict, '')
    #print()
    #print('elements_dict: ', elements_dict)
    #print()
    #bb()
    m = html_page(elements_dict)
    print(m)

if __name__ == '__main__':
    main(sys.argv)
