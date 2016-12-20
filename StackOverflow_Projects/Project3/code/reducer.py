#!/usr/bin/env python

import sys

def reducer():

	oldKey = None
	totalDays = 0.0
 	numCount = 0.0	
	for row in sys.stdin:
		data_mapped = row.split()
		if len(data_mapped) < 2:
			continue

		thisKey, thisData = data_mapped
		
		totalDays += float(thisData)
		numCount += 1

	print totalDays/numCount

if __name__ == "__main__":
        reducer()
