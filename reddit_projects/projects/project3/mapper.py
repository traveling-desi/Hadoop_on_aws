#!/usr/bin/env python

import sys
from datetime import datetime
#import xml.etree.ElementTree as ET

def mapper():
    fields = []
    may1 = datetime(2015, 5, 1)
    may31 = datetime(2015, 5, 31)
    for row in sys.stdin:
        # Strip whitespace from the row
        fields = row.strip().split('\t')
        if len(fields) != 8:
        	continue

	newfield = fields[2].lower()
	dt = datetime.utcfromtimestamp(float(fields[3])) 
	#print dt
	#print may1
	#print may31
	if dt  >= may1 and dt <= may31:
	#if fields[0] == 'nfl'and dt  > may1 and dt < may31:
		print dt.date(), newfield.count(' deflategate ') + newfield.count(' tom brady ')


if __name__ == "__main__":
	mapper()
