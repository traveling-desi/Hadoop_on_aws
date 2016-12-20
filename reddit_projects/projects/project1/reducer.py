#!/usr/bin/env python

import sys

def reducer():

	oldKey = None
	totalLove = 0.0000001
	totalHate = 0.0000001
	for row in sys.stdin:
		data_mapped = row.split()
		if len(data_mapped) != 3:
			continue

		thisKey, thisLove, thisHate = data_mapped

		#print data_mapped

		#print thisKey, thisLove, thisHate
		
		totalLove += float(thisLove)
		totalHate += float(thisHate)

		#print totalLove, totalHate

		if oldKey and thisKey != oldKey:
			lhi = (totalLove - totalHate)/(totalLove + totalHate)
			print oldKey, lhi
			totalLove = 0.0000001
			totalHate = 0.0000001

		oldKey = thisKey

	if oldKey:
		lhi = (totalLove - totalHate)/(totalLove + totalHate)
		print oldKey, lhi

if __name__ == "__main__":
        reducer()
