#!/usr/bin/env python3

"""
Simple python script to combine two or more suppression files (well any xml file really)

Usage:
./combine_suppression_files.py <OUTPUT FILENAME> <INPUT FILENAME 1> <INPUT FILENAME 2> ... <INPUT FILENAME n>
"""
import sys
from lxml import etree

def run(output_filename, input_filenames):
    output_xml = None
    for filename in input_filenames:
        this_file = etree.parse(filename)
        if output_xml is None:
            output_xml = etree.parse(filename)
        else:
            output_xml.getroot().extend(this_file.getroot())
    if output_xml is not None:
        output_xml.write(open(output_filename, 'wb'))

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2:])