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
	print fields[0], fields[2].lower().count(' love '), fields[2].lower().count(' hate ')


if __name__ == "__main__":
	mapper()
