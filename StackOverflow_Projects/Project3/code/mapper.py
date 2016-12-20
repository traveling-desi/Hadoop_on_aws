#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def mapper():
    for row in sys.stdin:
        # Strip whitespace from the row
        row = row.strip()
        # Make sure we're working with post data
        if not row.startswith('<row'):
            continue

        # Create the parser!
        parser = ET.fromstring(row)

	#print row
	#print parser.items()
	first = parser.get('CreationDate')
	first_dt = datetime.strptime(first, '%Y-%m-%dT%X.%f')

	second = parser.get('LastActivityDate')
	second_dt = datetime.strptime(second, '%Y-%m-%dT%X.%f')

	diff_dt = second_dt - first_dt

    	print 1, diff_dt.days


if __name__ == "__main__":
	mapper()
