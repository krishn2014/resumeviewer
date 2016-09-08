#!/usr/bin/python

import argparse
import json
from collections import OrderedDict

def display_resume(data):
    """
    Displays data for resume in proper format.

    Args:
        data: object of type dictionary representing the resume
    """
    print data

def show_resume(filename):
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