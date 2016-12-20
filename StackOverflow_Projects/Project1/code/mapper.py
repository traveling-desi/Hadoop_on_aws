#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

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
	if parser.get('AnswerCount') > 0:
		print parser.get('ViewCount'), parser.get('Score')


if __name__ == "__main__":
	mapper()
