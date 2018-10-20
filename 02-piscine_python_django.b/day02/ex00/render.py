#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    on importe le module sys
"""
import sys
import os
import re
import settings

""" 
    global variables
"""

def main(filename):
    """
    """
    output_filename = os.path.splitext(os.path.basename(filename))[0]
    output_filename += ".html"
    """ print('file is: %s ' % str(filename))        """
    """ print('file is: %s ' % str(output_filename)) """
    with open(output_filename, "w") as f_out:
        try:
            # do awesome stuff
            with open(filename, 'r') as f:
                try:
                    # do awesome stuff
                    for line in f:
                        f_out.write(line.format(
                        title=settings.title,
                        name=settings.name,
                        firstname=settings.firstname,
                        age=settings.age,
                        job=settings.job
                        ))
                except:
                    print('Error 1: Well darn.')
        except:
            print('Error: Well darn.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./render.py <file.template>')
        sys.exit(1)

    template_file = sys.argv[1]
    """ check if file exists and readble """
    if os.path.isfile(template_file) and os.access(template_file, os.R_OK):
        #print(template_file, " exists and is readable")
        pass
    else:
        print("Either file.template is missing or is not readable")
        sys.exit(1)

    """ check if file has template extension"""
    if re.search('\.template$', template_file, flags=re.IGNORECASE):
        #print('template extension')
        pass
    else:
        print("incorrect file template:", template_file, "should be a *.template file")
        sys.exit(1)

    main(template_file)
