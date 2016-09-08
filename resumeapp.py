#!/usr/bin/python

import argparse
import json
from collections import OrderedDict

INDENT_STR = '    '
MAX_LENGTH = 120

def limit_max_len(data, indentation, max_length=MAX_LENGTH):
    """
    Returns formats and returns multiline string if the lenght of 
    string given by data is > max_length

    Args:
        data: string
        indentation: indentation space
        max_length: maximum number of chars in single line
    """    
    buf = ''
    while len(data) > MAX_LENGTH:
        idx = data.rfind(' ', 0, MAX_LENGTH)
        buf += '%s\n%s' % (data[:idx], indentation)
        data = data[idx+1:]
    else:
        buf += data
    return buf

def display_resume(data, level = 0):
    """
    Displays data for resume in proper format.

    Args:
        data: object of type dictionary representing the resume
        level: indentation level
    """
    indentation = INDENT_STR * level
    buf = ''

    if isinstance(data, list):
        buf = ''
        for item in data:
            if isinstance(item, unicode):
                buf += "%s - %s\n" % (indentation, (limit_max_len(item, indentation+INDENT_STR)))
            else:
                buf += "%s\n" % (display_resume(item, level+1))
        return buf

    elif isinstance(data, dict):
        buf = ''
        for key in data:
            value = data[key]
            buf += "%s %s : " % (indentation, key)
            if isinstance(value, unicode):
                buf += display_resume(value, level+1)
            else:
                buf += '\n' + display_resume(value, level+1)
        return buf
    
    buf += "%s\n" % (limit_max_len(data, indentation))
    return buf

def show_resume(filename):
    """
    Displays resume denoted by teh filename.

    Args:
        filename: filename containing resume in json format
    """        
    with open(filename) as data_file: 
        data = json.load(data_file, object_pairs_hook=OrderedDict)

    print display_resume(data)        


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Resume viewer app.')
        parser.add_argument('file', help='name of file containing resume in json format')

        args = parser.parse_args()
        show_resume(args.file)
    except Exception as e:
        print "error: %s" % e
