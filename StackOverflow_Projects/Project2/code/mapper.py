#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

def mapper():
    tags = []
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
	tag = parser.get('Tags')
	if not tag == None:
		tags = tag.replace('<', ' ').replace('>', ' ').split()
		#print tags
		for tag in tags:
			print tag, parser.get('AnswerCount')


if __name__ == "__main__":
	mapper()
