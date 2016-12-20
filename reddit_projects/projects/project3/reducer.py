#!/usr/bin/env python

import sys

def reducer():

        oldKey = None
        totCount = 0
        for row in sys.stdin:
		data_mapped = row.split()

		#print data_mapped
		if len(data_mapped) != 2:
			continue

		thisKey, count = data_mapped
		#print thisKey, count


		if oldKey and thisKey != oldKey:
			print oldKey, totCount
			totCount = 0

		oldKey = thisKey
		totCount += int(count)

	if oldKey:
		print oldKey, totCount

if __name__ == "__main__":
        reducer()
