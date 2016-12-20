#!/usr/bin/env python

import sys

def reducer():

        oldKey = None
        totalUp = 0.0
        totalLen = 0.0
        count = 0
        for row in sys.stdin:
		data_mapped = row.split()
		if len(data_mapped) != 4:
			continue

		thisKey, _ , thisUp, thisLen = data_mapped

		if oldKey and thisKey != oldKey:
			print oldKey, count, totalUp/count, totalLen/count
			totalUp = 0.0
			totalLen = 0.0
			count = 0

		oldKey = thisKey
		totalUp += float(thisUp)
		totalLen += float(thisLen)
		count += 1

	if oldKey:
		print oldKey, count, totalUp/count, totalLen/count

if __name__ == "__main__":
        reducer()
