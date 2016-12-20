#!/usr/bin/env python

import sys
#import xml.etree.ElementTree as ET

def mapper():
    fields = []
    for row in sys.stdin:
        # Strip whitespace from the row
        fields = row.strip().split('\t')
        if len(fields) != 8:
        	continue
	print fields[1], 1, fields[4], len(fields[2].split(' '))


if __name__ == "__main__":
	mapper()
